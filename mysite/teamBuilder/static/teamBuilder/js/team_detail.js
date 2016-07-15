var teamID = window.location.href.split("/").pop();

$.get('/api/teams/' + teamID, function(result) {
	$('#name').html(result.name);
	$('#description').html(result.description);
	$('#description').html(result.description);
	var status = "normal ";
	if (result.is_confirmed)
		status += "confirmed ";
	if (result.is_special)
		status += "special";
	$('#status').html(status);
	$('#project').html(result.project);
	$.get(result.project, function(project){
		var projectId = project.url;
		projectId = projectId.split('/');
		projectId = projectId[projectId.length - 2];
		$('#project').html('<a href="/teambuilder/project/' + projectId + '/">' + project.title + '</a>');
	});
	for (candidate of result.candidate_list) {
		$.get(candidate, function(userprofile) {
			var outer = $("#team_detail_container");
			$("<div class=\"panel panel-default\"><div class=\"panel-heading\"><h3 class=\"panel-title\">team apply</h3></div><div class=\"panel-body\"><p>"
				+ userprofile.realname + ":message</p><a class=\"btn btn-default\" role=\"button\">agree</a></div></div>").appendTo(outer);
			// 问题 message去哪拿？
		});
	}
	for (member of result.member_list) {
		$.get(member, function(userprofile) {
			var outer = $('#member_list');
			$("<div class=\"col-md-3\"><div class=\"panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p>"
				+ userprofile.realname + "</p></div></div></div></div>").appendTo(outer);
		});
	}
});

$("#form_apply").attr("action", "/api/teams/" + teamID + "/join_apply");

$("#userId").val(sessionStorage.id);
// 问题 怎么拿userid？