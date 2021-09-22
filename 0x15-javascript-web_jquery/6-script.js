$('DIV#update_header').click(function () {
  $('header').change(function () {
    $(this).text('New Header!!!')
  }).change();
});
