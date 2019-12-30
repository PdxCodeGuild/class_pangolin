let num1 = document.getElementById('num1');
let num2 = document.getElementById('num2');
let operator = document.getElementById('operator');
let calulate = document.getElementById('calculate');
let result = document.getElementById('result');

function doMath() {
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    let answer;
    if (operator.value === '+') {
        answer = x + y;
    } else if (operator.value === '-') {
        answer = x - y;
    } else if (operator.value === '*') {
        answer = x * y;
    } else if(operator.value === '/') {
        answer = x / y;
    }
    result.innerText = "Answer:  " + answer;    
}

calulate.addEventListener('click', doMath);
num2.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        doMath();
    }
});
