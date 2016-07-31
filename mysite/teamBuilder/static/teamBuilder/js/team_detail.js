var teamID = window.location.href.split("/").pop();
var owner = null;

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

$.get('/api/teams/' + teamID, function(result) {
	$('#name').html(result.name);
	$('#description').html(result.description);
	$('#description').html(result.description);
    owner = result.owner;
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
	sessionStorage.candidate_list = result.candidate_list;
	sessionStorage.member_list = result.member_list;
	var candidate_list = result.candidate_list,
	    member_list = result.member_list;

    // console.log(member_list.length);
    if (member_list.length > 1) {
        if (!sessionStorage.userProfile in member_list)
            $('#apply_button').hide();
    } else {
        if (member_list.length == 1 && sessionStorage.userProfile == member_list)
            $('#apply_button').hide();
    }

    if (candidate_list.length > 1) {
        if (sessionStorage.userProfile in candidate_list)
            $('#apply_button').addClass('disabled');
        else {
            setApply();
        }
    } else {
        if (candidate_list.length == 1 && sessionStorage.userProfile == candidate_list) {
            // $('#apply_button').hide();
            $('#apply_button').addClass('disabled').removeClass('btn-primary').addClass('.btn-default');
            $('#apply_button').text('You have appled for this team');
        }
        else {
            setApply();
        }
    }

    if (sessionStorage.userProfile == owner) {
    	for (var candidate of candidate_list) {
    		$.get(candidate, function(userprofile) {
    			var outer = $("#team_detail_container");
                var userId = userprofile.owner;
                userId = userId.split('/');
                userId = userId[userId.length - 2];
    
    			$("<div class=\"panel panel-default\"><div class=\"panel-heading\"><h3 class=\"panel-title\">team apply</h3></div><div class=\"panel-body\"><p>"
    				+ userprofile.realname + ":  <a href=\"/teambuilder/user/" + userId + "\">Profile</a></p><a class=\"btn btn-default agree-button\" role=\"button\" url=\""
    				+ candidate + "\">agree</a></div></div>").appendTo(outer);
    			$('.agree-button:last').data('url', userprofile.url);
                $(".agree-button:last").click(function(e){
                	var url = $(e.currentTarget).data('url');
                    var member_list = sessionStorage.member_list;
                    member_list = member_list.split(',');
                    member_list.push(url);
                    // debugger
                    var candidate_list = sessionStorage.candidate_list;
                    candidate_list = candidate_list.split(',');
                    candidate_list.remove(url);
                    for (var i = 0; i < member_list.length; ++i) {
                        if (member_list[i] == '') member_list.remove(i);
                    }
                	$.ajax({
                		url: "/api/teams/" + teamID + '/', 
                		success: function(result) {
                		  // console.log(result);
                		  alert("添加成员成功！");
                		  location.reload();
                		},
                        error: function(response) {
                          var err = JSON.parse(response.responseText);
                          console.log(err);
                          if (err.non_field_errors) {
                            alert(err.non_field_errors[0]);
                          }
                        },
                		data: JSON.stringify({
                            candidate_list: candidate_list,
                            member_list: member_list,
                            project: result.project
                		}),
                        headers: {
                            'Authorization': 'Token ' + window.sessionStorage.token
                        },
                        method: 'PATCH',
                        contentType: 'application/json'
                	});
                });
    		});
    	}
    }
	sequence = 0;
	for (member of member_list) {
		$.get(member, function(userprofile) {
			var outer = $('#member_list');
            var memberId = userprofile.owner;
            console.log(memberId);
            memberId = memberId.split('/');
            memberId = memberId[memberId.length - 2];
			var memberBlock = $("<div class=\"col-md-3\"><div class=\"panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/teamBuilder/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p>"
				+ '<a href="/teambuilder/user/' + memberId + '">' + userprofile.realname + '</a>' + "</p></div></div></div></div>").appendTo(outer);
            if (member == sessionStorage.userProfile) memberBlock.css('color', 'red');
		});
	}
	if (!result.member_list){
		$("#member_list").css("display", "none");
	}

});

$("#form_apply").attr("action", "/api/teams/" + teamID + "/join_apply");

$("#userId").val(sessionStorage.id);

$(".info").click(function(e) {
	$(this).css("display", "none");
	$(this).siblings("input").css("display", "block");
	$(this).siblings("button").css("display", "block");
});

function setApply() {
    $("#apply_button").click(function(e){
        e.preventDefault();
        var url = sessionStorage.userProfile;
        var candidate_list = sessionStorage.candidate_list;
        if (typeof candidate_list == 'string') {
            candidate_list = candidate_list.split(',');
            // console.log(candidate_list);
            candidate_list.push(url);
        }
        console.log(candidate_list.length);
        for (var i = 0; i < candidate_list.length; ++i) {
            if (candidate_list[i] == '') candidate_list = candidate_list.remove(i); 
        }
        $.ajax({
            url: "/api/teams/" + teamID + '/', 
            success: function(result) {
              // console.log(result);
              alert("申请成功！");
              location.reload();
            },
            data: JSON.stringify({
                candidate_list: candidate_list
            }),
            headers: {
                'Authorization': 'Token ' + window.sessionStorage.token
            },
            method: 'PATCH',
            contentType: 'application/json'
        });
    });
}

$(".update-button").click(function(e) {
	var key = $(this).siblings("span").attr("id");
	var value = $(this).siblings("input").val();
	if (value == "") {
		alert("不能为空");
	} else {
        var data = {};
        data[key] = value;
		$.ajax({
    		url: "/api/teams/" + teamID + '/', 
    		success: function(result) {
    		  console.log(result);
    		  alert("更新成功！");
    		  location.reload();
    		},
    		data: JSON.stringify(data),
            headers: {
                'Authorization': 'Token ' + window.sessionStorage.token
            },
            method: 'PATCH',
            contentType: 'application/json'
    	});
	}
});

if (sessionStorage.userProfile != owner) $('.agree-button').hide();