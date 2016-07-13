var teamID = window.location.href.split("/").pop();

$.get('/api/teams/:id', function(result) {
	$('#name').val(result.name);
	$('#description').val(result.description);
	$('#description').val(result.description);
	var status = "normal ";
	if (result.is_confirmed)
		status += "confirmed ";
	if (result.is_special)
		status += "special";
	$('#status').val(status);
	$('#project').val(result.project);
	for (candidate in result.candidate_list) {
		$.get(candidate, function(userprofile) {
			var outer = $("#team_detail_container");
			$("<div class=\"panel panel-default\"><div class=\"panel-heading\"><h3 class=\"panel-title\">team apply //only for the team leader</h3></div><div class="panel-body"><p>"
				+ userprofile.realname + ":message</p><a class=\"btn btn-default\" role=\"button\">agree</a></div></div>").appendTo(outer);
			// 问题 message去哪拿？
		});
	}
	for (member in result.member_list) {
		$.get(member, function(userprofile) {
			var outer = $('#member_list');
			$("<div class=\"col-md-3\"><div class=\"panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p>
				+ userprofile.realname + "</p></div></div></div></div>").appendTo(outer);
		});
	}
});

$("#form_apply").attr("action", "/api/teams/" + teamID + "/join_apply");

$("#userId").val("");
// 问题 怎么拿userid？