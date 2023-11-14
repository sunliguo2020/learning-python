$(function(){
	$search_options = $('#search-options'),
    $items = $search_options.find('.items');
    $items.each(function() {
		var $this = $(this),
			_myHeight = $this.height();
		if (_myHeight > 28 && _myHeight <= 52) {
			$this.parent().height(48);
			$this.next(".more-btn").text('').removeClass('clicked');
		}
		else if(_myHeight > 52)
		{
			$this.parent().height(48);
		}
		else
		{
			$this.parent().height(28);	
			$this.next(".more-btn").text('').removeClass('clicked');
		}
		if (_myHeight > 54) {
			$this.next('a.more-btn').show().on('click', function() {
				var _this = $(this);
				if (_this.hasClass('clicked')) {
					$this.parent().height(48);
					_this.text('更多').removeClass('clicked');
				} else {
					$this.parent().height(_myHeight);
					_this.text('收起').addClass('clicked');
				}
			});
		}
	});	
	
	var $box = $('#priceform'),
    	$form = $box.find('form'),
        $input = $form.find('input[type=text]'),
        $hp = $("#hidden_price");
	$input.on('focus', function() {
        $box.addClass('focus');
     });
	$(document).on("click", function(e) {
        if ($(e.target).parents("#priceform").length == 0) {
 			$box.removeClass('focus');
		}
	});
})