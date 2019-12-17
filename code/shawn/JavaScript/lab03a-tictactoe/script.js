class Player{
    constructor(input_name, input_symbol){
        this.name = input_name;
        this.token = input_symbol;
    }
}
class Game{
    constructor(){
        this.board =    [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']];
    }


    printBoard(){
        let print_str = "*********** tic tac toe ***********\n";

        for (let y = 0; y < this.board.length; y++){
            for (let x = 0; x < this.board[y].length; x++){

                // for manipulating DOM
                let cellCoord = `c${x}${y}`;
                let cell = document.getElementById(cellCoord);
                cell.innerText = this.board[y][x];

                // for printing text version
                if (x == 1){
                    print_str += `| ${this.board[y][x]} |`;
                }
                else {
                    print_str += ` ${this.board[y][x]} `;

                }
            }
            print_str += '\n';
        }
        print_str += "***********************************"
        console.log(print_str);
        alert(print_str);
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

    isGameOver(){
        if (this.calcWinner() || this.isFull()){
            return true;
        }
        return false;
    }

    getValidXYCoord(player){
        while(true){
            
            let user_input = prompt(`${player.name}'s turn.  Please input x,y coordinates for ${player.token} symbol: `);

            let x_input = user_input[0];
            let y_input = user_input[2];
            if(this.board[y_input][x_input] === ' '){
                return [x_input, y_input]
            } else {
                alert(`${x_input},${y_input} already taken!  Please enter new coordinates.`)
            }
        }
    }

    move(x,y,player_token){
        this.board[y][x] = player_token;
    }
    
    playTurn(player, coord){
        // add that player's token to the game board logic
        this.board[coord[2]][coord[1]] = player.token;
        // add visual representation of token.  remove button.
        document.getElementById(coord).innerHTML = player.token;
    }
}



function gameInit(){
    userName1 = prompt("Enter player 1 name: ");
    userName2 = prompt("Enter player 2 name: ");
    let player1 = new Player(userName1, 'X');
    let player2 = new Player(userName2, 'O');
    let gameBoard = new Game();

    return [gameBoard, player1, player2];
}

function go(cellCoord){

    if(counter % 2 == 1){
        var player = player1;
        var nextPlayer = player2;
    } else if (counter % 2 == 0) {
        var player = player2;
        var nextPlayer = player1;
    }

    gameBoard.playTurn(player, cellCoord);
    // gameBoard.printBoard();

    if(gameBoard.calcWinner()){
        document.getElementById('message').innerText = `Player ${gameBoard.calcWinner()} wins!`;
        let buttons = document.getElementsByTagName('button');
        for (let button of buttons){
            button.disabled = true;
        }
        document.getElementById('play-again').innerHTML = '<br><button onclick=location.reload()>Play again?</button>';

    } else if (gameBoard.isFull()){
        document.getElementById('message').innerText = `The board is full...players tie.`;
        document.getElementById('play-again').innerHTML = '<br><button onclick=location.reload()>Play again?</button>';
    } else {
        counter++;
        document.getElementById('message').innerText = `${nextPlayer.name}'s turn.  Click a button to place your ${nextPlayer.token} symbol: `
    }
}

let start = gameInit();
let gameBoard = start[0];
let player1 = start[1];
let player2 = start[2];
var counter = 1;
document.getElementById('message').innerText = `${player1.name}'s turn.  Click a button to place your ${player1.token} symbol: `

// class Game{
//     constructor(){
//         this.board =    [[' ',' ',' '],
//                          [' ',' ',' '],
//                          [' ',' ',' ']];
//     }


//     printBoard(){
//         let print_str = "*********** tic tac toe ***********\n";

//         for (let y = 0; y < this.board.length; y++){
//             for (let x = 0; x < this.board[y].length; x++){

//                 // for manipulating DOM
//                 let cellCoord = `c${x}${y}`;
//                 let cell = document.getElementById(cellCoord);
//                 cell.innerText = this.board[y][x];

//                 // for printing text version
//                 if (x == 1){
//                     print_str += `| ${this.board[y][x]} |`;
//                 }
//                 else {
//                     print_str += ` ${this.board[y][x]} `;

//                 }
//             }
//             print_str += '\n';
//         }
//         print_str += "***********************************"
//         console.log(print_str);
//         alert(print_str);
//     }

//     move(x,y,player_token){
//         this.board[y][x] = player_token;
//     }

//     calcWinner(){
//         let symbols = ['X', 'O'];
//         for (let symbol of symbols){
//             if (this.board[0][0] == symbol && this.board[0][1] == symbol && this.board[0][2] == symbol){
//                 return symbol;
//             }
//             else if (this.board[1][0] == symbol && this.board[1][1] == symbol && this.board[1][2] == symbol){
//                 return symbol;
//             }
//             else if (this.board[2][0] == symbol && this.board[2][1] == symbol && this.board[2][2] == symbol){
//                 return symbol;
//             }
//             else if (this.board[0][0] == symbol && this.board[1][0] == symbol && this.board[2][0] == symbol){
//                 return symbol;
//             }
//             else if (this.board[0][1] == symbol && this.board[1][1] == symbol && this.board[2][1] == symbol){
//                 return symbol;
//             }
//             else if (this.board[0][2] == symbol && this.board[1][2] == symbol && this.board[2][2] == symbol){
//                 return symbol;
//             }

//             else if (this.board[0][0] == symbol && this.board[1][1] == symbol && this.board[2][2] == symbol){
//                 return symbol;
//             }
//             else if (this.board[0][2] == symbol && this.board[1][1] == symbol && this.board[2][0] == symbol){
//                 return symbol;
//             }
//         }
//     }

//     isFull(){
//         for (let y = 0; y < this.board.length; y++){
//             for (let x = 0; x < this.board[y].length; x++){
//                 if (this.board[x][y] === ' '){
//                     return false;
//                 }
//             }
//         }
//         return true;
//     }

//     isGameOver(){
//         if (this.calcWinner() || this.isFull()){
//             return true;
//         }
//         return false;
//     }

//     getValidXYCoord(player){
//         while(true){
//             document.getElementById('message').innerText = `${player.name}'s turn.  Please input x,y coordinates for ${player.token} symbol: `
//             let user_input = prompt(`${player.name}'s turn.  Please input x,y coordinates for ${player.token} symbol: `);

//             let x_input = user_input[0];
//             let y_input = user_input[2];
//             if(this.board[y_input][x_input] === ' '){
//                 return [x_input, y_input]
//             } else {
//                 alert(`${x_input},${y_input} already taken!  Please enter new coordinates.`)
//             }
//         }
//     }

//     playTurn(player){
//         let coord = this.getValidXYCoord(player);
//         this.move(coord[0],coord[1],player.token);
//     }
// }
// //repl loop
// let run_flag = true
// while (run_flag){

//     let start = gameInit();
//     let gameBoard = start[0];
//     let player1 = start[1];
//     let player2 = start[2];

//     let counter = 1;

//     while(!gameBoard.isGameOver()){
//         if(counter % 2 == 1){
//             gameBoard.playTurn(player1);
//         } else if (counter % 2 == 0) {
//             gameBoard.playTurn(player2);
//         }
//         counter++;
//         gameBoard.printBoard();
//     }

//     if(gameBoard.calcWinner()){
//         alert(`Player ${gameBoard.calcWinner()} wins!`);
//     } else if (gameBoard.isFull()){
//         alert(`The board is full...${player1.name} ties ${player2.name}`);
//     }

//     let user_input = prompt("Play again?  Please enter (y) or (n): ");
//     if (user_input === 'n'){
//         alert("Game over.");
//         run_flag = false;
//     }
// }
