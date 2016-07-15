$('#sign-in').click(function(event) {
    event.preventDefault();
    
    // 创建FormData对象
    var data = new FormData(),
        username = $('#inputUsername3').val(),
        password = $('#inputPassword3').val();
    data.append('username', username);
    data.append('password', password);
    
    $.ajax({
    	url: '/api-token-auth/',
    	// data: {
     //        username: username,
     //        password: password,
    	// },
        data: data,
    	method: 'post',
    	context: document.body,
    	processData: false, // 使用FormData对象时要加这个字段
    	contentType: false,
        // contentType: 'application/json', //同上
    	success: function(result) {
            if (result.token) {
                window.sessionStorage.token = result.token;
                getCurrentUser(function(result) {
                    window.sessionStorage.username = result.username;
                    window.sessionStorage.userURL = result.url;
                    window.sessionStorage.userProfile = result.user_profile;
                    window.sessionStorage.email = result.email;
                    var url = result.url;
                    var sp = url.split('/');
                    window.sessionStorage.id = sp[sp.length - 2];
                    window.location.href = '/teambuilder/';                   
                });
            } else {
            	alert('用户名或密码错误');
            }
    	}
    });
});