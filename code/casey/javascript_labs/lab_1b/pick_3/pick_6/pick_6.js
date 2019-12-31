/* Lab 1: Pick 6 - Version 1

Purpose/goal: Have the computer play pick6 many times and determine net balance.

    - Generate a list of 6 random numbers representing the winning ticket - D

    - Start your balance at 0 - D

    - Loop 1000 times, for each loop:
    
        - Generate a list of 6 random numbers representing the ticket - D
    
        - Subtract 2 from your balance (you bought a ticket) - D
    
        - Find how many numbers match - D
    
        - Add to your balance the winnings from your matches - D
    
        - After the loop, print the final balance - D 
    */

// define balance
let balance = 0;

// define winner ticket
const winner = Array.from({length: 6}, () => Math.floor(Math.random() * 100));

// pick6 function
function pick6() { 
    return Array.from({length: 6}, () => Math.floor(Math.random() * 100));
}

// create ticket matching function
function num_matches(a, b) {
    var x = 0;
    for (let i=0; i < b.length; ++i) {
        if (a[i] === b[i]) {
            x += 1;
        }
    }
    return x;
}

// create lottery loop 
let lottery = 0 
while (lottery < 1000) {
    balance -= 2;
    ticket = pick6();
    x = num_matches(ticket, winner);
    const win_arr = [0, 4, 7, 100, 5000, 1000000, 25000000];
    balance += win_arr.indexOf(x);
    lottery += 1;
}

document.write(`After playing the lottery 1000 times, you have a blanace of ${balance} dollars.` + "<br>Very sad.");
