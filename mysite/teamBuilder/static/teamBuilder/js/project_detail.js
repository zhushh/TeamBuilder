var projectID = window.location.href.split("/");
  projectID = projectID[projectID.length -2];
var teamID = "";

/*
Array.prototype.remove = function(val) {
  var i = 0;
  for (i = 0; i < this.length; ++i) {
  	if (this[i] == val) break;
  }
  if (this.length > 0 && i < this.length) {
  	this.splice(i, 1);
  }
  return this;
}*/

$.get('/api/projects/' + projectID , function(result) {

	$('#title').html(result.title);
	var ownername="";
	var userId = result.owner;
  userId = userId.split('/');
	userId = userId[userId.length - 2];
	$.get('/api/userprofiles/'+ userId , function(ownerResult){
		ownername = ownerResult.realname;   
    console.log(ownerResult.team_captain);
    var count =1;
    for (teamId in ownerResult.team_captain) {
        count++;
    }
    console.log(count);
    teamID = count; 
   console.log(teamID);
  var outer = $('#create_team');
  $("<a href = \"" + '/teambuilder/project/createTeam/' + teamID + "\" class=\"btn btn-primary\" role = \"button\"> createTeam</a>").appendTo(outer);

    $('#owner').html(ownername);
	});    

    console.log(result.school);
	$('#school').html(result.school);
	$('#description').html(result.description);
 
	var outer = $("#teams");
  console.log(result.team_enrolled);
	for (team in result.team_enrolled) {
    console.log(result.team_enrolled);
		$.get(team, function(teamresult){
			var name = teamresult.name;
			var teamId = teamresult.url;
            teamId = teamId.split('/');
            teamId = teamId[teamId.length - 2];
			$("<li class=\"list-group-item\">" +"<a class=\"btn btn-default\" href=\""
                    + '/teambuilder/team/' + teamId + "\" role=\"button\">"
                    + name +"</a></li>").appendTo(outer);
		});
	}

});

$(".info").click(function(e) {
    $(this).css("display", "none");
    $(this).siblings("input").css("display", "block");
    $(this).siblings("button").css("display", "block");
});
$(".update-button").click(function(e) {
    var key = $(this).siblings("span").attr("id");
    var value = $(this).siblings("input").val();
    if (value == "") {
        alert("不能为空");
    } else {
        var data = {};
        data[key] = value;
        $.ajax({
            url: "/api/projects/" + projectID, 
            success: function(result) {
              console.log(result);
              alert("更新成功！");
              location.reload();
            },
            data: data,
            headers: {
                'Authorization': 'Token ' + window.sessionStorage.token
            },
            method: 'PATCH',
            contentType: 'application/x-www-form-urlencoded',
            dataType: 'json'
        });
    }
});
