#!/usr/bin/node
/* comment for the checker */

const axios = require('axios').default;
const fs = require('fs');

const url = process.argv[2];
const fileStore = process.argv[3];

axios.get(url)
  .then((res) => {
    const contenido = res.data;

    fs.writeFile(fileStore, contenido, err => {
      if (err) { console.error(err); }
    });
  });
