// random redirect javascript lab 5
// written by Rhornberger
// last updated december 27 2019

let links=new Array();
links[1]="https://www.paleorunningmomma.com/spinach-artichoke-dip-paleo-vegan/"
links[2]="https://www.paleorunningmomma.com/pepperoni-pizza-loaded-sweet-potato-fries-paleo/"
links[3]="https://www.paleorunningmomma.com/bacon-zucchini-fritters-paleo-whole30/"


// window.location=links[myRandom];


window.setTimeout(5000)
let seconds = 5;

let myRandom=Math.round(Math.random()*links.length);

function countdown() {
    seconds = seconds -1;
    if (seconds < 0) {
        window.location=links[myRandom];
    } else {
        document.getElementById("countdown").innerHTML = seconds;
        window.setTimeout("countdown()", 1000);
    }
}      


countdown();