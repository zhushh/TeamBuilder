var userID = window.location.href.split("/").pop();

Array.prototype.remove = function(val) {
  var i = 0;
  for (i = 0; i < this.length; ++i) {
    if (this[i] == val) break;
  }
  if (this.length > 0 && i < this.length) {
    this.splice(i, 1);
  }
  return this;
}

$.get("/api/users/" + userID+'/', function(result){
    $.get(result.user_profile, function(profileResult){
        console.log(profileResult.description);
        $("#description").html(profileResult.description);


        var projectIndex = 1;
    	var outer = $("#project_list");
        console.log(profileResult.project_published);
    	for (projectterm of profileResult.project_published){
            console.log(projectterm);
            projectIndex++;
            var projectId = projectterm.split("/");
            projectId = projectId[projectId.length-2];
            console.log(projectId);
    		$.get('/api/projects/'+ projectId+ '/',function(projectResult){
    			var title = projectResult.title;
    			var school = projectResult.school;
                var department = projectResult.department;
                var major = projectResult.major;
                var description = projectResult.description;
                console.log(projectResult);
                console.log(school);
                console.log(department);
                console.log(major);

    			$("<div class=\"col-lg-2 \">" + "<a href=\""+'/teambuilder/project/' + projectId + "\">"+
                    "<div class=\"panel panel-default\" style=\"margin-top: 10px;\">"+
                     "<h2 style=\"display:inline-block\"><span>Title: </span>"+title+"</h2>"+
                     "<div class=\"panel-body\">"+"<div style=\"display:inline-block\">"+ 
                    "<p><span>Major: </span>"+major+
                    "<p><span>Department: </span>"+department+
                    "<p><span>School: </span>"+school+
                     "<p><span>Description: </span>"+description+
                     "</div></div></div></a></div>"
                    ).appendTo(outer);
    		});
    	}
        console.log(projectIndex);
        var outer2 = $("#createproject");
        $("<a class=\"btn btn-default\" href=\""+'/teambuilder/project/create/'+"\" role=\"button\" class =\"btn btn-primary\">create New project</a>").appendTo(outer2);

    });
});

