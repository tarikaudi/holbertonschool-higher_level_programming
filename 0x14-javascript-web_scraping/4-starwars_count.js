#!/usr/bin/node
/* comment for the checker */

const axios = require('axios').default;

const url = process.argv[2];

axios.get(url)
  .then((res) => {
    const movies = res.data.results;
    let count = 0;

    for (const arr of movies) {
      const perso = arr.characters;
      for (const personaje of perso) {
        if (personaje.includes('18')) { count++; }
      }
    }
    console.log(count);
  })
  .catch((err) => {
    console.log(err);
  });
