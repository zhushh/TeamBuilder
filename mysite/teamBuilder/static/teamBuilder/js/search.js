var url = window.location.pathname;

if (url != '/teambuilder/') {
	$('.search-block').hide();
} else {
	$('.search-block').show();
}

$('#search').click(function() {
	var items = $('.project-item');
	for (item of items) {
		if ($(item).find())
	}
});