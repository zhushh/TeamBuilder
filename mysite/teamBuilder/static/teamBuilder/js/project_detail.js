var projectID = window.location.href.split("/").pop();

$.get('/api/project/:id', function(result) {
	$('#title').val(result.title);
	$('#owner').val(result.owner);
	$('#deadline').val(result.deadline);
	$('#school').val(result.school);
	$('#description').val(result.description);
	var outer = $("#teams");
	for (teamID in result.team_enrolled) {
		$.get("/api/teams/" + teamID, function(teamresult){
			var name = teamresult.name;
			$("<li class=\"list-group-item\">" +"<a class=\"btn btn-default\" href=\""
                    + team + "\" role=\"button\">"
                    + name +"</a>"+ "</li>").appendTo(outer);
		});
	}
	$.get('')
});