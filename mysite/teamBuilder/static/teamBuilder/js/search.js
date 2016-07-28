var url = window.location.pathname;

if (url != '/teambuilder/') {
	$('.search-block').hide();
} else {
	$('.search-block').show();
}

$('#search').click(function(e) {
	var items = $('.project-item'),
	    key = $('#search-key').val();
	items.show();
	for (var i = 0; i < items.length; ++i) {
		var item = items[i];
		$(item).find('.title').each(function() {
			var title = this.innerText;
			if (title.indexOf(key) == -1) $(item).hide();
		});
		// console.log($($(item).find('.title')[0]).innerHTML);
	}
});