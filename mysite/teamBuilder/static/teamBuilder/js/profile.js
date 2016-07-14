var userID = window.location.href.split("/").pop();

$.get("/api/users/" + userID, function(result){
    $("#username").val(result.username);
    $("#email").val(result.email);
    $.get(result.user_profile, function(profileResult){
        $("#realname").val(profileResult.realname);
        $("#phone").val(profileResult.phone);
        $("#school").val(profileResult.school);
        $("#department").val(profileResult.department);
        $("#major").val(profileResult.major);
        $("#grade").val(profileResult.grade);
        $("#description").val(profileResult.description);
        $("#phone").val(profileResult.phone);
        var outer = $("#teams");
        for (team in result.team_member.concat(result.captain)) {
            $.get(team, function(fuck){
                var name = fuck.name;
                $("<a class=\"btn btn-default\" href=\""
                    + team + "\" role=\"button\">"
                    + name +"</a>").appendTo(outer);
            });
        }
    });
});

$.get("/api/comments/" + userID, function(result) {
    var outer = $("#profile_outer");
    for (comment in result) {
        $("<div class=\"personal_info_comment panel panel-default\" style=\"margin-top: 10px;\"><div class=\"panel-body\"><img src=\"/static/images/touxiang.jpg\" alt=\"avator\" style=\"width:55px;height:55px;display:inline-block;\"/><div style=\"display:inline-block\"><p><span class=\"personal_info_comment_time\">"
            + result.time + "</span></br><span class=\"personal_info_comment_owner\">"
            + result.owner + "</span><span>:</span><span class=\"personal_info_comment_content\">"
            + result.content + "</span></p></div></div></div>").appendTo(outer);
    }
});
