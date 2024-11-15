#!/usr/bin/node

const request = require("request");

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// API URL for the Star Wars movies
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log("Error:", error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    // For each character in the "characters" list, request the character data
    movieData.characters.forEach((url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.log("Error:", error);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.log(
      "Failed to retrieve movie data. HTTP Status Code:",
      response.statusCode
    );
  }
});
