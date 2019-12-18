// simple calculator made with javascript.  Takes user numbers input and desired math operators to do a simple equation. //

var x = parseFloat(prompt("What is the first number?"));
var y = parseFloat(prompt("What is the second number?"));
var z = prompt("What is the operation you wish to perform");

function calculator (x,y,z) {
    
    if (z === "+") {
        alert(x+y);
    }
    else if (z === "-") {
        alert(x-y);
    }
    else if (z === "*") {
        alert(x*y);
    }
    else if (z === "/") {
        alert(x/y);
    }
    else if (z === "%") {
        alert(x%y);
    }
    else if (z === "**"){
        alert(x**y);
    }
    else {
        alert("There was an error with your input");
    }
    console.log(x,y,z);
}
calculator(x,y,z);