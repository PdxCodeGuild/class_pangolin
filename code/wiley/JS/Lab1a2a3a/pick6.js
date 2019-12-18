/* Pick 6 lab in javascript.  Gonna be weird.  Lets give it a go!
A ticket costs $2. 
If 1 number match you in $4. 
2 numbers, you win $7. 
3 you win $100
4 you win $50,000
5, you win 1,000,000
6, you win 25,000,000.

First, generate a winning ticket.  This will be an array of 6 numbers. 
Then generate an amount of user tickets to compare against the winner.  
Subtract $2 for each ticket "bought" and add the winnings back into the pot.

*/
// var winner = Math.round(Math.random() *100) 
// console.log("example is " + winner)

// creating an array called winningArray, of 6 numbers between 0-100 //
var winningArray = []
for (let i=0; i<6; i++) {
   winningArray.push(Math.round(Math.random() *100)); 
}
console.log("winning ticket = " + winningArray);





//function to create an array of six numbers between 0-99 //
function pickSix() {
    let betArray = []
    for (let i=0; i<6; i++) {
        betArray.push(Math.round(Math.random() *100)); 
     }
    console.log("Bet array is " + betArray)
    return betArray
}

// function to compare the values of two arrays, and return the number of matches. //
function compareTickets(a,b) {
    let match = []
    for (let i=0;i<a.length; i++)
    if (a[i] == b[i])
        match.push(a[i])
        console.log("current matches = " + match)
        console.log(match.length + " length of matches")
    return match.length
}
// a function to cash out based on matches //
function cashOut(x) {
    let cash = 0;
    if (x === 0) {
        console.log("Cash out money is " + cash)
        return 0;
    }
    else if (x === 1) {
        cash += 4; 
        console.log("Cash out money is " + cash)
        return cash;
    }
    else if (x === 2) {
        cash += 7;
        console.log("Cash out money is " + cash)
        return cash;
    }
    else if (x === 3) {
        cash += 100;
        console.log("Cash out money is " + cash)
        return cash;
    }
    else if (x === 4) {
        cash += 50000;
        console.log("Cash out money is " + cash)
        return cash;
    }
    else if (x === 5) {
        cash += 1000000;
        console.log("Cash out money is " + cash)
        return cash;
    }
    else if (x === 6) {
        cash += 25000000;
        console.log("Cash out money is " + cash)
        return cash;
    }   
    else {
        return console.log("What just happened?");
    }
    

}
// cashOut(compareTickets(winningArray,pickSix()));

let money = 0;
let attempts = 0;
let attempt_times = parseInt(prompt("How many bets would you like to make? "));
let i = 0;
while (i < attempt_times) {
    money -= 2;
    i++;
    money += cashOut(compareTickets(winningArray,pickSix()));
}
document.write("You won " + money + " dollars in the pick 6 lotto! ");