#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  if (!err && res.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        throw err;
      }
    });
  }
});
