class Player{
    constructor(input_name, input_symbol){
        this.name = input_name;
        this.token = input_symbol;
        this.wins = 0;
    }
}
class Game{
    constructor(){
        this.board =    [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']];
    }

    calcWinner(){
        let symbols = ['X', 'O'];
        for (let symbol of symbols){
            if (this.board[0][0] == symbol && this.board[0][1] == symbol && this.board[0][2] == symbol){
                return symbol;
            }
            else if (this.board[1][0] == symbol && this.board[1][1] == symbol && this.board[1][2] == symbol){
                return symbol;
            }
            else if (this.board[2][0] == symbol && this.board[2][1] == symbol && this.board[2][2] == symbol){
                return symbol;
            }
            else if (this.board[0][0] == symbol && this.board[1][0] == symbol && this.board[2][0] == symbol){
                return symbol;
            }
            else if (this.board[0][1] == symbol && this.board[1][1] == symbol && this.board[2][1] == symbol){
                return symbol;
            }
            else if (this.board[0][2] == symbol && this.board[1][2] == symbol && this.board[2][2] == symbol){
                return symbol;
            }
            else if (this.board[0][0] == symbol && this.board[1][1] == symbol && this.board[2][2] == symbol){
                return symbol;
            }
            else if (this.board[0][2] == symbol && this.board[1][1] == symbol && this.board[2][0] == symbol){
                return symbol;
            }
        }
    }

    isFull(){
        for (let y = 0; y < this.board.length; y++){
            for (let x = 0; x < this.board[y].length; x++){
                if (this.board[x][y] === ' '){
                    return false;
                }
            }
        }
        return true;
    }

    playTurn(player, coord){
        // add that player's token to the game board logic
        this.board[coord[2]][coord[1]] = player.token;
        // add visual representation of token.  remove button.
        document.getElementById(coord).innerHTML = `<img src="player${player.token}.png"/>`;
    }
}

function gameInit(){
    let player1 = new Player(document.getElementById('player1-name').value, 'X');
    let player2 = new Player(document.getElementById('player2-name').value, 'O');
    let gameBoard = new Game();

    return [gameBoard, player1, player2];
}

function go(cellCoord){

    //update player names
    player1.name = document.getElementById('player1-name').value
    player2.name = document.getElementById('player2-name').value

    if(counter % 2 == 1){
        var player = player1;
        var nextPlayer = player2;
    } else if (counter % 2 == 0) {
        var player = player2;
        var nextPlayer = player1;
    }
    
    gameBoard.playTurn(player, cellCoord);
    let winnerChar = gameBoard.calcWinner();
    if(winnerChar){
        let winnerName = '';
        if(winnerChar == 'X') {
            winnerName = player1.name;
            player1.wins++;
            document.getElementById('player1-wins').innerText = player1.wins;
        } 
        else {
            winnerName = player2.name;
            player2.wins++;
            document.getElementById('player2-wins').innerText = player2.wins;
        }
        document.getElementById('message').innerText = `${winnerName} wins!`;
        let buttons = document.querySelectorAll('.cell-button');
        for (let button of buttons){
            button.remove();
        }
        document.getElementById('play-again').innerHTML = '<br><button onclick=newGame() class="play-again-button">Play again?</button>';

    } else if (gameBoard.isFull()){
        document.getElementById('message').innerText = `The board is full...tie.`;
        document.getElementById('play-again').innerHTML = '<br><button onclick=newGame() id="play-again-button">Play again?</button>';
    } else {
        counter++;
        document.getElementById('message').innerText = `${nextPlayer.name}'s turn.  Click a button to place your ${nextPlayer.token} symbol: `
    }
}

// function for starting new game
function newGame(){
    start = gameInit();
    gameBoard = start[0];
    counter = 1;
    document.getElementById('message').innerText = `${player1.name}'s turn.  Click a button to place your ${player1.token} symbol: `
    document.querySelector(".grid").innerHTML = `
    <div class='grid'>
        <div id="c00">
            <button onclick="go('c00')" class="cell-button">Play Here!</button>
        </div>
        <div id="c10">
            <button onclick="go('c10')" class="cell-button">Play Here!</button>
        </div>
        <div id="c20">
            <button onclick="go('c20')" class="cell-button">Play Here!</button>
        </div>
        <div id="c01">
            <button onclick="go('c01')" class="cell-button">Play Here!</button>
        </div>
        <div id="c11">
            <button onclick="go('c11')" class="cell-button">Play Here!</button>
        </div>
        <div id="c21">
            <button onclick="go('c21')" class="cell-button">Play Here!</button>
        </div>
        <div id="c02">
            <button onclick="go('c02')" class="cell-button">Play Here!</button>
        </div>
        <div id="c12">
            <button onclick="go('c12')" class="cell-button">Play Here!</button>
        </div>
        <div id="c22">
            <button onclick="go('c22')" class="cell-button">Play Here!</button>
        </div>
    </div>`

    // remove play again button
    document.getElementById('play-again-button').remove();
}
//manually setup first game
let start = gameInit();
let gameBoard = start[0];
let player1 = start[1];
let player2 = start[2];
var counter = 1;
document.getElementById('message').innerText = `${player1.name}'s turn.  Click a button to place your ${player1.token} symbol: `


