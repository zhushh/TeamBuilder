// if (window.sessionStorage.username && true) {
if (window.sessionStorage.token) {
	$('.unlogined').hide();
	var msg = 'Welcome, ' + window.sessionStorage.username + '!',
	    id = window.sessionStorage.id;
	$('.logined').append($('<li class="presentation"><a href="/teambuilder/user/' + id + '">' + msg + '</a></li>'));
	$('.logined').append($('<li class="presentation logout"><a href="/teambuilder/logout">Logout</a></li>'));
	$('.logined').append($('<li class="presentation"><a href="/teambuilder/project/create">Create Project</a></li>'));
} else {
	$('.logined').hide();
}

$('.logout').click(function(e) {
	e.preventDefault();
	window.sessionStorage.clear();
	window.location.href = '/teambuilder/logout';
});

getCurrentUser = function(callback) {
	if (window.sessionStorage.token) {
		$.ajax({
			url: '/api/users/current/',
            method: 'get',
            headers: {
            	'Authorization': 'Token ' + window.sessionStorage.token
            },
            success: callback
		});
	} else {
		console.log('you have not logined');
	}
}