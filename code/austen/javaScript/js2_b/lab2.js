// let winningTicket = document.getElementById("winningTicket");
// let guesses = document.getElementById("guesses");
// let play = document.getElementById("play");
// let totalBallance = document.getElementById("totalBallance");
let resetGame = document.getElementById("reset");
let ticketView = document.getElementById("ticketView").style.display = "none";
let totals = document.getElementById("totals").style.display = "none";
let main = document.getElementById("main").style.display = "none";

let ticket;
let plays;
let total_spent = -0;
let ballance = 0;
// creats a array of random numbers between 0-99
function game(){
    yourTicket();
    tickets();
    total_spent = -0;
    ballance = 0;
    totalSpent.innerText = total_spent;
    totalBallance.innerText = ballance;
    guesses.value = null;
    document.getElementById("totals").style.display = "none"
    document.getElementById("main").style.display = "block";
}
function yourTicket(){
    ticket = [];
    while(ticket.length < 6){
        var r = Math.floor(Math.random() *100) +1;
        if(ticket.indexOf(r) === -1) ticket.push(r);
    }
    if (ticket) {
        document.getElementById("ticketView").style.display = "block";
        winningTicket.innerText = ticket;
    }
//while loop for 100000 tries to match the ticket with your_ticket
}

function tickets(){
    let num = 0;
    plays = guesses.value;
    while(num < plays){
    // incrimenting the ballance down 2 dollars totoal spent up by 2 dollars
        ballance -= 2;
        total_spent += 2;

    //creating the winning ticket numbers 100000 times 
        var your_ticket = [];
        while(your_ticket.length < 6){
            var r = Math.floor(Math.random() *100) +1;
            if(your_ticket.indexOf(r) === -1) your_ticket.push(r);
        }
    //checking to see if the numbers in both arrarys match up
        var same =(a1, a2) => your_ticket.reduce((a, c) => a + ticket.includes(c), 0);
    //giving them a if else if statment to inccrease the ballance and ticket winnings
        if (same(your_ticket,ticket) === 1) {
            ballance +=4;
        }else if (same(your_ticket,ticket) === 2) {
            ballance += 7;
        }else if (same(your_ticket,ticket) === 3) {
            ballance += 100;
        }else if (same(your_ticket,ticket) === 4) {
            ballance += 50000;
        }else if (same(your_ticket,ticket) === 5) {
            ballance += 1000000;
        }else if (same(your_ticket,ticket) === 6) {
            ballance += 25000000;
        }

        num++;
        document.getElementById("totals").style.display = "block"
    }
// this is putting the text on the page in the proper positions
totalSpent.innerText = total_spent;
totalBallance.innerText = ballance;
}
play.addEventListener('click', tickets);
totalBallance.addEventListener('click', totalBallance);
resetGame.addEventListener('click', game);