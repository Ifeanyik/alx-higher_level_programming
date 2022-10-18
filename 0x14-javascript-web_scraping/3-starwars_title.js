#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const options = { json: true };
request(url, options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (!error && response.statusCode === 200) {
    console.log(body.title);
  }
});
