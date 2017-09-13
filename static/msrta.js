$(document).ready(function(){
  $('div.goal').click(function(){
    var _this = $(this)
    if (_this.hasClass('color-black')){
      _this.addClass('color-blue').removeClass('color-black')
    } else if(_this.hasClass('color-blue')){
      _this.addClass('color-green').removeClass('color-blue')
    } else {
      _this.addClass('color-black').removeClass('color-green')
    }
  });
  $(".goaltrial a").click(function(e) {
    e = e || window.event
    //IE9 & Other Browsers
    if (e.stopPropagation) {
      e.stopPropagation();
    }
    //IE8 and Lower
    else {
      e.cancelBubble = true;
    }
  });
});
