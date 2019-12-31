let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let oper = document.getElementById("oper");
let calc = document.getElementById("btn");
let results = document.getElementById("results");

function calculate() {
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    var answer
    if (oper.value === "+") {
        answer = x + y;
    }
    else if (oper.value === "-") {
        answer = x - y;
    }
    else if (oper.value === "/") {
        answer = x / y;
    }
    else if (oper.value === "*") {
        answer = x * y;
    }
    if (answer) {
        results.innerText = answer;
    }
};

// num1.addEventListener("input", calculate);
// oper.addEventListener("input", calculate);
// num2.addEventListener("input", calculate);
calc.addEventListener("click", calculate);