// simple calculator made with javascript.  Takes user numbers input and desired math operators to do a simple equation. //

// var x = parseFloat(prompt("What is the first number?"));
// var y = parseFloat(prompt("What is the second number?"));
// var z = prompt("What is the operation you wish to perform");
let num1 = document.getElementById("num1");
let oper = document.getElementById("operator");
let num2 = document.getElementById("num2");
let ans = document.getElementById("answer")
// console.log(x,y,z)
let calcbtn = document.getElementById("calc-btn");

function calculator () {
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    let z = oper.value
    let answer;
    console.log(x)
    if (z === "+") {
        answer = (x)+(y);
    }
    else if (z === "-") {
        answer = (x-y);
    }
    else if (z === "*") {
        answer = (x*y);
    }
    else if (z === "/") {
        answer = (x/y);
    }
    else if (z === "%") {
        answer = (x%y);
    }
    else if (z === "**"){
        answer = (x**y);
    }
    else {
        alert("There was an error with your input");
    }
    if (answer) {
        ans.innerText = answer;
    }
}

calcbtn.addEventListener('click', calculator);
