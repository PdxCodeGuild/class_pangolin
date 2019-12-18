let num1 = document.getElementById("first-num");
let num2 = document.getElementById("second-num");
let oper= document.getElementById("oper");
let btn = document.getElementById("calc-btn");
let result = document.getElementById("result");
let results = document.getElementById("results");

// this will upate the result field with the result without recording to the list
function doTheMath(event){
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    let answer;
    if (oper.value === '+') {
        answer = x + y;
    }
    else if (oper.value === '-') {
        answer = x - y;
    }
    else if (oper.value === '*') {
        answer = x * y;
    }
    else if (oper.value === '/') {
        answer = x / y;
    }
    if (answer) result.innerText = answer;
}

// this will update the result field and record to list at same time
function doTheMathRecorded(event){
    let x = parseFloat(num1.value);
    let y = parseFloat(num2.value);
    let answer;
    if (oper.value === '+') {
        answer = x + y;
    }
    else if (oper.value === '-') {
        answer = x - y;
    }
    else if (oper.value === '*') {
        answer = x * y;
    }
    else if (oper.value === '/') {
        answer = x / y;
    }
    if (answer) result.innerText = answer;
    let li = document.createElement("li");
    li.innerText = answer;
    results.appendChild(li);
}

num1.addEventListener('input', doTheMath);
oper.addEventListener('input', doTheMath);
num2.addEventListener('input', doTheMath);

// calculate result when enter pressed on second number field
num2.addEventListener('keydown', function(event){
    console.log(event.key);     // shows what event is pressed in the console
    if (event.key === "Enter"){
        doTheMathRecorded();
    }
});

btn.addEventListener('click', doTheMathRecorded);



