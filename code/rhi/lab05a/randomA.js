// random redirect javascript lab 5
// written by Rhornberger
// last updated december 27 2019

function random_3() {
    let links=new Array();
    links[1]="https://www.paleorunningmomma.com/spinach-artichoke-dip-paleo-vegan/"
    links[2]="https://www.paleorunningmomma.com/pepperoni-pizza-loaded-sweet-potato-fries-paleo/"
    links[3]="https://www.paleorunningmomma.com/bacon-zucchini-fritters-paleo-whole30/"

    let myRandom=Math.round(Math.random()*links.length);
    window.location=links[myRandom];
}
