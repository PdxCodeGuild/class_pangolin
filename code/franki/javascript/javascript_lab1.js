
function chooseRandomObject() {
    let gameObjects = ['rock', 'paper', 'scissors']
    let randomInteger = Math.floor(Math.random() * 3)
    return gameObjects[randomInteger]
}

function determineWinner(result) {
    if (result === 'win') {
        return("You won!")
    } else if (result === 'lose') {
        return("You lost!")
    } else if (result === 'tie') {
        return("It's a tie!")
    } else {
        return("Error")
    }
}

function playGame(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return 'tie'
    }  else if (userChoice === 'rock') {
            if (computerChoice === 'scissors') {
                return 'lose'
            } else {
                return 'win'
            }
    }   else if (userChoice === 'scissors') {
            if (computerChoice === 'rock') {
                return 'lose'
            } else {
                return 'win'
            }
    }   else if (userChoice === 'paper') {
            if (computerChoice === 'rock') {
                return 'win'
            }   else {
                return 'lose'
            }
        }
}

let userChoice = prompt("Rock, paper, or scissors? ");
let computerChoice = chooseRandomObject();
let result = playGame(userChoice, computerChoice);
let winner = determineWinner(result);
alert(`Your choice: ${userChoice}\n
Computer choice: ${computerChoice}\n
${winner}`);