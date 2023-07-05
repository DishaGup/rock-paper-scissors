// script.js

// Get references to the game elements
const userChoiceElement = document.getElementById("user-choice");
const computerChoiceElement = document.getElementById("computer-choice");
const gameResultElement = document.getElementById("game-result");
const userWinsElement = document.getElementById("user-wins");
const computerWinsElement = document.getElementById("computer-wins");
const drawsElement = document.getElementById("draws");
const rockButton = document.getElementById("rock");
const paperButton = document.getElementById("paper");
const scissorsButton = document.getElementById("scissors");

// Function to handle button clicks and initiate the game
function play(choice) {
  // Display the user's choice

  userChoiceElement.textContent = choice;

  // Send the user's choice to the server for processing
  fetch("/play", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ choice: choice }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Update the computer's choice and game result based on the server's response
    
      computerChoiceElement.textContent = data.computer_choice;
      gameResultElement.textContent = data.result;
      userWinsElement.textContent = data.user_wins;
      computerWinsElement.textContent = data.computer_wins;
      drawsElement.textContent = data.draws;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}



// Add event listeners to the buttons
rockButton.addEventListener("click", () => play("rock"));
paperButton.addEventListener("click", () => play("paper"));
scissorsButton.addEventListener("click", () => play("scissors"));
