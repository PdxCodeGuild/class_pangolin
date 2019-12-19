let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let oper = document.getElementById("oper");
let calc = document.getElementById("btn");

function calculate() {
    if (document.getElementById('oper').value === "+") {
        console.log(num1 + num2);
        return num1 + num2;
    }
    if (document.getElementById('oper').value === "-") {
        console.log(num1 - num2);
        return num1 - num2;
    }
    if (document.getElementById('oper').value === "/") {
        console.log(num1 / num2);
        return num1 / num2;
    }
    if (document.getElementById('oper').value === "*") {
        console.log(num1 * num2);
        return num1 * num2;
    }
};

calc.addEventListener("click", calculate());