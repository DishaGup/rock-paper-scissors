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
function updateScores(scores) {
    userWinsElement.textContent = `User: ${scores.user_wins}`;
    computerWinsElement.textContent = `Computer: ${scores.computer_wins}`;
    drawsElement.textContent = `Draws: ${scores.draws}`;
}

function play(choice) {
    // Make a POST request to the '/play' endpoint with the user's choice
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ choice }),
    })
    .then((response) => response.json())
    .then((data) => {
        // Access the specific values from the response
        const computerChoice = data.computer_choice;
        const computerWins = data.computer_wins;
        const draws = data.draws;
        const gameResult = data.result;
        const userWins = data.user_wins;

        // Update the game elements with the results
        userChoiceElement.textContent = choice;
        computerChoiceElement.textContent = computerChoice;
        gameResultElement.textContent = gameResult;
        updateScores({ user_wins: userWins, computer_wins: computerWins, draws });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function restartGame() {
    // Make a POST request to the '/restart' endpoint to reset the scores
    fetch('/restart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((data) => {
        // Update the game elements with the reset scores
        userChoiceElement.textContent = "";
        computerChoiceElement.textContent = "";
        gameResultElement.textContent = "";
        updateScores({ user_wins: 0, computer_wins: 0, draws: 0 });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Add event listeners to the buttons
rockButton.addEventListener("click", () => play("rock"));
paperButton.addEventListener("click", () => play("paper"));
scissorsButton.addEventListener("click", () => play("scissors"));
