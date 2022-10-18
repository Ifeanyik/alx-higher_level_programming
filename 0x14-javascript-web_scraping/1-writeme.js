#!/usr/bin/node
const fs = require('fs');
const f_string = fs.writeFile(process.argv[2], process.argv[3], 'utf8', function(err) {
  if (err)
	console.error(err);
});
