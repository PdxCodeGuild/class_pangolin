let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let oper = document.getElementById("oper");
let btn = document.getElementById("calc-btn");

function doTheMath() {
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    let answer
    if (oper.value === "+") {
        answer = x + y;
    } else if (oper.value === "-") {
        answer = x - y;
    } else if (oper.value === "*") {
        answer = x * y;
    } else if (oper.value === "/") {
        answer = x / y;
    }
    // let li = document.createElement("li");
    // li.innerText = answer;
    // results.appendChild(li);
    if (answer) {
    results.innerText = answer;
    }
}

btn.addEventListener('click', doTheMath);
num1.addEventListener('input', doTheMath);
num2.addEventListener('input', doTheMath);
oper.addEventListener('input', doTheMath);

