(function($){
  $(function(){

    $('.button-collapse').sideNav();

  }); // end of document ready

  //  Get last GitHub commit.
  if ($('.github-commit').length) {
      $.ajax({
        url: "https://api.github.com/repos/axiacore/generator-django-axiacore/commits/master",
        dataType: "json",
        success: function (data) {
          var sha = data.sha,
              date = $.timeago(data.commit.author.date);
          $('.github-commit').find('.date').html(date);
          $('.github-commit').find('.sha').html(sha).attr('href', data.html_url);
        }
      });
    }

    // Handle image zoom.
    $('.materialboxed').materialbox();

})(jQuery); // end of jQuery name space
