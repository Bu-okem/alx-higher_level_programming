// fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    for (const i of data.results) {
      $('UL#list_movies').append('<li>' + i.title + '</li>');
    }
  }
);
