(function ($) {
  // color box
  $(document).ready(function(){
          //Examples of how to assign the ColorBox event to elements
          $(".group1").colorbox({rel:'group1'});
          $(".group2").colorbox({rel:'group2', transition:"fade"});
          $(".group3").colorbox({rel:'group3', transition:"none", width:"75%", height:"75%"});
          $(".group4").colorbox({rel:'group4', slideshow:true});
          $(".ajax").colorbox();
          $(".youtube").colorbox({iframe:true, innerWidth:425, innerHeight:344});
          $(".iframe").colorbox({iframe:true, width:"80%", height:"80%"});
        });
})(jQuery);
<!--script executions -->
(function ($) {
    // portfolio hover effect
    $(function(){
      $('.ch-item').bind('hover', function(e){});
    });
  })(jQuery);
  (function ($) {
    //back to top
    $(function() {
      $(window).scroll(function() {
        if($(this).scrollTop() > 300) {
          $('#toTop').fadeIn();
          $('#feedback-div').fadeIn();
        } else {
          $('#toTop').fadeOut();
          $('#feedback-div').fadeOut();
        }
      });
      $('#toTop').click(function() {
        $('body,html').animate({scrollTop:0},1000);
      });
      fontSize("#fontRsz", "p,h2,h4,div", 9, 12, 20);
    });
  })(jQuery);
function fontSize(container, target, minSize, defSize, maxSize) {
  /*Editable settings*/
  var maxCaption = "Make font size larger"; //title for largefont button
  var minCaption = "Make font size smaller"; //title for smallFont button
  var defCaption = "Make font size default"; //title for defaultFont button
  //Now we'll add the font size changer interface in container
  smallFontHtml = "<a href='javascript:void(0);' class='smallFont' title='" + minCaption +"'></a> ";
  largeFontHtml = "<a href='javascript:void(0);' class='largeFont' title='" + maxCaption +"'></a> ";
  defFontHtml = "<a href='javascript:void(0);' class='defaultFont' title='" + defCaption +"'></a> ";
  $(container).html("Font Size :"+ defFontHtml+ largeFontHtml + smallFontHtml);
  //Read cookie & sets the fontsize
  if ($.cookie != undefined) {
    var cookie = target.replace(/[#. ]/g,'');
    var value = $.cookie(cookie);
    if (value !=null) {
      $(target).css('font-size', parseInt(value));
    }
  }
  //on clicking small font button, font size is decreased by 1px
  $(container + " .smallFont").click(function(){
    curSize = parseInt($(target).css("font-size"));
    newSize = curSize - 1;
    if (newSize >= minSize) {
      $(target).css('font-size', newSize);
    }
    if (newSize <= minSize) {
      $(container + " .smallFont").addClass("sdisabled");
    }
    if (newSize < maxSize) {
      $(container + " .largeFont").removeClass("ldisabled");
    }
    updatefontCookie(target, newSize); //sets the cookie
  });
  //on clicking default font size button, font size is reset
  $(container + " .defaultFont").click(function(){
    $(target).css('font-size', defSize);
    $(container + " .smallFont").removeClass("sdisabled");
    $(container + " .largeFont").removeClass("ldisabled");
    updatefontCookie(target, defSize);
  });
  //on clicking large font size button, font size is incremented by 1 to the maximum limit
  $(container + " .largeFont").click(function(){
    curSize = parseInt($(target).css("font-size"));
    newSize = curSize + 1;
    if (newSize <= maxSize) {
      $(target).css('font-size', newSize);
    }
    if (newSize > minSize) {
      $(container + " .smallFont").removeClass("sdisabled");
    }
    if (newSize >= maxSize) {
      $(container + " .largeFont").addClass("ldisabled");
    }
    updatefontCookie(target, newSize);
  });
  function updatefontCookie(target, size) {
    if ($.cookie != undefined) { //If cookie plugin available, set a cookie
      var cookie = target.replace(/[#. ]/g,'');
      $.cookie(cookie, size);
    }
  }
}


/********** GA js *********/
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-45241284-1', 'sscnasscom.org');
ga('send', 'pageview');