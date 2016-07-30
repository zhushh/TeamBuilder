//$('#projectID').val(window.location.href.split("/").pop());
/*
if (window.sessionStorage.token) {
    id = window.sessionStorage.id;
}
$.get('/api/userprofile/'+ id ,function(userresult){
    var count = 1;
    for (project in userresult.project_published){
        count+=1;
    }
});
var projected = count;
*/
$('#create_project').click(function(e) {
    console.log('Enter here.');
	e.preventDefault();
    var data = {
            title: $('#title').val(),
            description: $('#description')[0].value,
            school:$('#school').val(),
            department:$('#department').val(),
            major:$('#major').val(),
            min_num:$('#min_num').val(),
            max_num:$('#max_num').val()
       
           
        };

    console.log(data);
    $.ajax({
    	url: '/api/projects/', 
    	success: function(result){    
            if (result.url) {
            	alert('创建成功');
            	var id = result.url;
            	id = id.split('/');
            	id = id[id.length - 2];
            	window.location.href = '/teambuilder/project/' + id +'/'; 
            }
            else{
                alert('wrong operate');
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