#!/usr/bin/node
/* comment for checker */

const axios = require('axios').default;

const id = process.argv[2];

const titleExtract = (id) => {
  axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
    .then((res) => {
      console.log(res.data.title);
    })
    .catch((err) => {
      console.log(err);
    });
};

titleExtract(id);
