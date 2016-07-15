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
        for (team in profileResult.team_member.concat(result.captain)) {
            $.get(team, function(fuck){
                var name = fuck.name;
                $("<a class=\"btn btn-default\" href=\""
                    + team + "\" role=\"button\">"
                    + name +"</a>").appendTo(outer);
            });
        }
    });
});

