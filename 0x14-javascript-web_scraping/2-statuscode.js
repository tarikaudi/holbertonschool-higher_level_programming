#!/usr/bin/node
/* comment for the cheker */
const axios = require('axios').default

const url = process.argv[2];

axios.get(url)
  .then((response) => { console.log(`code: ${response.status}`); })
  .catch((err) => {
    console.log(`code: ${err.response.status}`);
  });
