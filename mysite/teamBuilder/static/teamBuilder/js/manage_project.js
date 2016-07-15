var userID = window.location.href.split("/").pop();

$.get("/api/users/" + userID, function(result){
    $.get(result.user_profile, function(profileResult){
        $("#description").val(profileResult.description);
    	var outer = $("#project_list");
    	for (project in profileResult.project_published){
    		$.get("/api/projects/" + project,function(projectResult){
    			var title = projectResult.title;
    			var deadline = projectResult.deadline;
    			var school = projectResult.school;
    			$("<div class=\"col-lg-2 column ui-sortable\">").appendTo(outer);
    			$("<a href=\"\">").appendTo(outer);
    			$("<div class=\"panel panel-default\" style=\"margin-top: 10px;\">").appendTo(outer);
    			$("<h2 style=\"display:inline-block\">"+project1+"</h2>").appendTo(outer);
    			$("<div class=\"panel-body\">").appendTo(outer);
    			$("<div style=\"display:inline-block\">").appendTo(outer);
    			$("<p>"+title+"</p>").appendTo(outer);
    			$("<p>"+deadline+"</p>").appendTo(outer);
    			$("<p>"+school+"</p>").appendTo(outer);
    			$("</div>"+"</div>"+"</div>" + "</a>" + "</div").appendTo(outer);    			
    		});
    	}
    });
});
