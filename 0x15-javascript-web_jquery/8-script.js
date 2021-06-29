$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films) {
    $.each(films.results, function (index, film) {
      const li = $('<li></li>').text(film.title);
      $('UL#list_movies').append(li);
    });
  });
});
