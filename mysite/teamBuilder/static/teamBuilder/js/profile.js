var userID = window.location.href.split("/").pop();
var msgs = null;

$.get("/api/users/" + userID, function(result){
    $("#username").html(result.username);
    $("#email").html(result.email);
    $.get(result.user_profile, function(profileResult){
        $("#realname").html(profileResult.realname);
        $("#phone").html(profileResult.phone);
        $("#school").html(profileResult.school);
        $("#department").html(profileResult.department);
        $("#major").html(profileResult.major);
        $("#grade").html(profileResult.grade);
        $("#description").html(profileResult.description);
        $("#phone").html(profileResult.phone);
        
        msgs = profileResult.msg_sent;
        for (url of msgs) {
            $.get(url, function(result) {
                console.log(result);
                var outer = $("#profile_outer");
                $("<div class=\"personal_info_comment panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p><span class=\"personal_info_comment_time\">"
                    + result.time + "</span></br><span class=\"personal_info_comment_owner\">"
                    + result.owner + "</span><span>:</span><span class=\"personal_info_comment_content\">"
                    + result.content + "</span></p></div></div></div>").appendTo(outer);
            });
        }


        var outer = $("#teams");
        for (team of profileResult.team_candidate) {
            $.get(team, function(fuck){
                var name = fuck.name;
                var teamId = fuck.url;
                teamId = teamId.split('/');
                teamId = teamId[teamId.length - 2];
                $("<a class=\"btn btn-default\" href=\""
                    + '/teambuilder/team/' + teamId + "\" role=\"button\">"
                    + '队伍: ' + name +"</a>").appendTo(outer);
            });
        }
    });
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
        $.ajax({
            url: "/api/userprofiles/" + userID + '/', 
            success: function(result) {
              console.log(result);
              alert("更新成功！");
              location.reload();
            },
            data: JSON.stringify({
                key: value,
            }),
            headers: {
                'Authorization': 'Token ' + window.sessionStorage.token
            },
            method: 'PATCH',
            contentType: 'application/json'
        });
    }
});
