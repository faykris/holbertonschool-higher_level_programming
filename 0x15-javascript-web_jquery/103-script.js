$(document).ready(function () {
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.keyCode === 13) {
      e.preventDefault();
      $.get('https://fourtonfish.com/hellosalut/?lang=' +
        $('INPUT#language_code').val(), function (value) {
        $('DIV#hello').text(value.hello);
      });
    }
  });
  $('INPUT#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' +
      $('INPUT#language_code').val(), function (value) {
      $('DIV#hello').text(value.hello);
    });
  });
});
