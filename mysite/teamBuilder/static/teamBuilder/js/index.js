$.ajax({
	url: '/api/projects/', 
	success: function(data){
        let results = data.results;
        for (var i = 0; i < data.count; ++i) {
            var title = '<p class="bg-primary">' + '项目: ' + results[i].title + '</p>',
                owner = '<p class="bg-success">' + '专业: ' + results[i].department + '</p>',
                description = '<p class="bg-success">' + '描述: ' + results[i].description + '</p>',
                school = '<p class="bg-success">' + '学校: ' + results[i].school + '</p>';
            var id = results[i].url;
            id = id.split('/');
            id = id[id.length - 2];
            var url = '"' + '/teambuilder/project/' + id + '"';
            var block = $('<a' + ' href=' + url + ' class="project-item"><div><div class="col-sm-3">' + title + owner + description + school + '</div></div></a>');
            $('#projects').append(block);
        }
    },
    // headers: {
    //     'Authorization': 'Token ' + window.sessionStorage.token
    // },
    method: 'get',
});
