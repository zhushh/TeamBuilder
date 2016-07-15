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
				+ userprofile.realname + ":message</p><a class=\"btn btn-default agree-button\" role=\"button\" url=\""
				+ candidate + "\">agree</a></div></div>").appendTo(outer);
		});
	}
	for (member of result.member_list) {
		$.get(member, function(userprofile) {
			var outer = $('#member_list');
			$("<div class=\"col-md-3\"><div class=\"panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p>"
				+ userprofile.realname + "</p></div></div></div></div>").appendTo(outer);
		});
	}
	if (!result.member_list){
		$("#member_list").css("display", "none");
	}
});

$("#form_apply").attr("action", "/api/teams/" + teamID + "/join_apply");

$("#userId").val(sessionStorage.id);

$("#appy_button").click(function(){
	$.post("/api/teams/" + teamID + "/join_apply", fcuntion(result) {
		alert("申请成功！");
		location.reload();
	});
});

$(".agree-button").click(function(){
	$this = $(this);
	$.get($this.attr("url"), function(result) {
		$.get(result.owner, function(result) {
			$.post("/api/teams/" + teamID + "/join_accept", {"userId": result._id}, function(result) {
				alert("success!");
				location.reload();
			});
		});
	});
});
