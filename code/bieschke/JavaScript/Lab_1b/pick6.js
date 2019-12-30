let winners = [];
let expenses = 0;
let earnings = 0;
let ticket_master = [];

function roi(earnings, expenses) {
    alert('ROI is: ')
    return ((earnings - expenses)/expenses);
}

let generate = document.getElementById('generate', function() {
    console.log("generate!")
    for (let i=0; i<6; i++) {
        let dig = Math.round(Math.random()*100);
        ticket.push(dig);
    }
    console.log(ticket)
}); 

let bigsix = document.getElementById('bigsix', function() {
    console.log("Big Six!")
    for (let i=0; i<6; i++) {
        let winner = Math.round(Math.random()*100);
        winners.push(winner);
    }
    console.log(winners);

    let matches = [];

    for (let i=0; i<winners.length; i++) {
        console.log(ticket[i], winners[i])
        if (ticket[i] === winners[i]) {
            matches.push(ticket[i]);
            alert('matches='+matches);
        }
    }

    if (matches != []) {
        if (matches.length === 1) { 
            earnings +=4; }
        else if (matches.length === 2) { 
            earnings +=7; }
        else if (matches.length === 3) { 
            earnings +=100; }
        else if (matches.length === 4) { 
            earnings +=50000; }
        else if (matches.length === 5) { 
            earnings +=1000000; }
        else if (matches.length === 6) { 
            earnings +=25000000; }
        }
    ticket_master.push(ticket);
});

// let lions=0;
// while (lions < 5) {
//     lions++;
//     expenses -=2;
//     let ticket = [];

//     for (let i=0; i<6; i++) {
//         let dig = Math.round(Math.random()*100);
//         ticket.push(dig);
//     }
//     // ticket=winners;
//     alert(ticket);

//     let matches = [];

//     for (let i=0; i<winners.length; i++) {
//         console.log(ticket[i], winners[i])
//         if (ticket[i] === winners[i]) {
//             matches.push(ticket[i]);
//             alert('matches='+matches);
//         }
//     }

//     if (matches != []) {
//         if (matches.length === 1) { 
//             earnings +=4; }
//         else if (matches.length === 2) { 
//             earnings +=7; }
//         else if (matches.length === 3) { 
//             earnings +=100; }
//         else if (matches.length === 4) { 
//             earnings +=50000; }
//         else if (matches.length === 5) { 
//             earnings +=1000000; }
//         else if (matches.length === 6) { 
//             earnings +=25000000; }
//         }
//     ticket_master.push(ticket);
// }
// alert(roi(earnings, expenses));
