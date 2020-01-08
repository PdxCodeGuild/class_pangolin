
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

function rps(e) {
    console.log(e.target.id)
    let selectedObject = e.target.id
    let userChoice = selectedObject;
    let computerChoice = chooseRandomObject();
    let result = playGame(userChoice, computerChoice);
    let winner = determineWinner(result);
    // let div = document.getElemebtById("text")
    alert(`Your choice: ${userChoice}\n
    Computer choice: ${computerChoice}\n
    ${winner}`);   

}

let rockBtn = document.getElementById("rock");
let paperBtn = document.getElementById("paper");
let scissorsBtn = document.getElementById("scissors");

rockBtn.addEventListener('click', rps);
paperBtn.addEventListener('click', rps);
scissorsBtn.addEventListener('click', rps);