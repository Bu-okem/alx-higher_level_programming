#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
