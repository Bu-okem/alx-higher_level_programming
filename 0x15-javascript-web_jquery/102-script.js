// fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const service = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const lang = $('INPUT#language_code').val();
    const url = service + lang;
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
