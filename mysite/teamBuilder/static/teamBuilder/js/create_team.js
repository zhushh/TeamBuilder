$('#teamID').val(window.location.href.split("/").pop());

$('#create-team').click(function(e) {
	e.preventDefault();
	var tags = [];
	for (var i = 1; i <= 3; ++i) {
		var tag = $('#tag' + i);
	    if (tag.is(':checked')) {
            tags.push(tag.val());
	    }
    }
    var data = {
            name: $('#teamname').val(),
            tags: tags,
            description: $('#desc')[0].value,
            project: 'http://' + window.location.host + '/api/projects/' + $('#teamID').val() + '/',
            is_confirmed: false,
            is_special: false
        };
    // console.log(data);
    $.ajax({
    	url: '/api/teams/', 
    	success: function(result){    
            if (result.url) {
            	alert('创建成功');
            	var id = result.url;
            	id = id.split('/');
            	id = id[id.length - 2];
            	window.location.href = '/teambuilder/team/' + id; 
            }
        },
        headers: {
            'Authorization': 'Token ' + window.sessionStorage.token
        },
        method: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data)
    });
});