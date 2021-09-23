$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' +
      $('INPUT#language_code').val(), function (value) {
      $('DIV#hello').text(value.hello);
    });
  });
});
