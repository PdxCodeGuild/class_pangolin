// function randomNumber(min, max) {
//     return Math.floor(Math.random() * (max - min) + min);
// }
// document.write("random number")

// document.write(randomNumber(1,100) );

// var ballance = 0;
// var winning_numbers = 0;
// var num = 0;
// var totoal_spent = 0;


// creats a array of random numbers between 0-99
var ticket = [];
while(ticket.length < 6){
    var r = Math.floor(Math.random() *100) +1;
    if(ticket.indexOf(r) === -1) ticket.push(r);
}
document.write('The ticket to match is: '+ ticket);
// console.log(arr);
total_spent = 0;
let num = 0;
let ballance = 0;
//while loop for 100000 tries to match the ticket with your_ticket
while(num <= 100000){
// incrimenting the ballance down 2 dollars totoal spent up by 2 dollars
    ballance -= 2;
    total_spent += 2;

//creating the winning ticket numbers 100000 times 
    var your_ticket = [];
    while(your_ticket.length < 6){
        var r = Math.floor(Math.random() *100) +1;
        if(your_ticket.indexOf(r) === -1) your_ticket.push(r);
    }
    // console.log(your_ticket);
    // var same = your_ticket.find(val => ticket.includes(val) );
    // console.log(same)
//checking to see if the numbers in both arrarys match up
    var same =(a1, a2) => your_ticket.reduce((a, c) => a + ticket.includes(c), 0);
    // console.log(same(your_ticket,ticket));
//giving them a if else if statment to inccrease the ballance and ticket winnings
    // console.log(num);
    if (same(your_ticket,ticket) === 1) {
        console.log("you win $4");ballance +=4;
    }else if (same(your_ticket,ticket) === 2) {
        console.log("you win $7");ballance += 7;
    }else if (same(your_ticket,ticket) === 3) {
        console.log("you win $100");ballance += 100;
    }else if (same(your_ticket,ticket) === 4) {
        console.log("you win $50,000");ballance += 50000;
    }else if (same(your_ticket,ticket) === 5) {
        console.log("you win $1,000,000");ballance += 1000000;
    }else if (same(your_ticket,ticket) === 6) {
        console.log("you win $25,000,000");ballance += 25000000;
    }

    num++;
    
}
//writing it out on the page
document.write("<br> The total spent is: "+ '$' + total_spent);
document.write("<br> The ballance is: " +'$' + ballance);
// document.write(same);
//     // console.log(same)


// }