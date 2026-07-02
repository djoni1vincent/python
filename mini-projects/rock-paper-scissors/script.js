const getComputerChoice = function () {
  let i = Math.floor(Math.random() * 3) + 1;
  if (i === 1) {
    return "rock";
  } else if (i === 2) {
    return "paper";
  } else {
    return "scissors";
  }
};

const getHumanChoice = function () {
  return prompt("Rock, Paper, or Scissors?").toLowerCase();
};

function playGame() {
  function playRound(humanChoice, computerChoice) {
    if (humanChoice === "rock" && computerChoice === "rock") {
      return "Tie";
    } else if (humanChoice === "paper" && computerChoice === "paper") {
      return "Tie";
    } else if (humanChoice === "scissors" && computerChoice === "scissors") {
      return "Tie";
    } else if (humanChoice === "rock" && computerChoice === "scissors") {
      return "You win!";
    } else if (humanChoice === "rock" && computerChoice === "paper") {
      return "You lose!";
    } else if (humanChoice === "paper" && computerChoice === "rock") {
      return "You win!";
    } else if (humanChoice === "paper" && computerChoice === "scissors") {
      return "You lose!";
    } else if (humanChoice === "scissors" && computerChoice === "paper") {
      return "You win!";
    } else if (humanChoice === "scissors" && computerChoice === "rock") {
      return "You lose!";
    } else {
      return "write rock, paper or scissors";
    }
  }
  let humanScore = 0;
  let computerScore = 0;

  for (let i = 0; i < 5; i++) {
    let humanChoice = getHumanChoice();
    let computerChoice = getComputerChoice();

    let result = playRound(humanChoice, computerChoice);
    if (result === "You win!") {
      humanScore++;
    } else if (result === "You lose!") {
      computerScore++;
    }
    console.log(
      `Round ${
        i + 1
      }: You chose ${humanChoice}, Computer chose ${computerChoice} → ${result}`
    );
  }

  console.log("Итоговый счёт:", humanScore, "-", computerScore);
}
playGame();
