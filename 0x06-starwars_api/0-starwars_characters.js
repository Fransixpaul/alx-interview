#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie: ${response.statusCode}`);
    return;
  }

  // Parse the movie data
  const data = JSON.parse(body);
  const characters = data.characters;

  // Fetch character names sequentially
  fetchCharacterNames(characters, 0);
});

// Function to fetch character names in order
function fetchCharacterNames (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    // Fetch the next character
    fetchCharacterNames(characters, index + 1);
  });
}
