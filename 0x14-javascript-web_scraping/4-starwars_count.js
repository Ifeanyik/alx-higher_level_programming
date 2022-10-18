#!/usr/bin/node
const request = require('request');
const options = {
  json: true,
  url: process.argv[2]
};
let charcount = 0;
request(options, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  if (!err && res.statusCode === 200) {
    for (const vara in body.results) {
      for (const charac in body.results[vara].characters) {
        if (body.results[vara].characters[charac] === 'https://swapi-api.hbtn.io/api/people/18/') {
          charcount++;
        }
      }
    }
    console.log(charcount);
  }
});
