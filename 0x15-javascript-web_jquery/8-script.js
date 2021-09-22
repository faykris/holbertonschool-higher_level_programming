$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movies) {
    $.each(movies.results, function (key, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
