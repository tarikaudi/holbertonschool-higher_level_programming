$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  const name = data.name;
  $('DIV#character').text(name);
});
