#!/usr/bin/node

// Importing necessary modules
const argv = process.argv;
const request = require('request');

// Base URL for the Star Wars API films endpoint
const filmsUrl = 'https://swapi-api.hbtn.io/api/films/';

// Constructing the URL for the specified movie based on the command-line argument
const movieUrl = `${filmsUrl}${argv[2]}/`;

// Making a request to fetch data for the specified movie from the Star Wars API
request(movieUrl, function (error, response, body) {
  // Checking for errors during the request
  if (!error) {
    // Parsing the JSON response body
    const movieData = JSON.parse(body);
    // Extracting the list of characters from the movie data
    const characters = movieData.characters;

    // Checking if characters are present in the movie data
    if (characters && characters.length > 0) {
      // Initiating the character request process
      const limit = characters.length;
      // Starting character request from the first character
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    // Handling errors during the request
    console.log('Error:', error);
  }
});

// Function to make requests for character data recursively
function CharRequest(idx, url, characters, limit) {
  // Base case: Stop recursion when all characters have been processed
  if (idx === limit) {
    return;
  }

  // Making a request for character data
  request(url, function (error, response, body) {
    // Checking for errors during the request
    if (!error) {
      // Parsing the JSON response body
      const characterData = JSON.parse(body);
      // Printing the name of the character
      console.log(characterData.name);
      // Incrementing index for the next character request
      idx++;
      // Recursively calling the function for the next character
      CharRequest(idx, characters[idx], characters, limit);
    } else {
      // Handling errors during the request
      console.error('Error:', error);
    }
  });
}
