let num1 = document.getElementById("first-num");
let num2 = document.getElementById("second-num");
let oper= document.getElementById("oper");
let btn = document.getElementById("calc-btn");
let results = document.getElementById("result");

btn.addEventListener('click', function(){
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
    let li = document.createElement("li");
    li.innerText = `${x} ${oper.value} ${y} = ${answer}`;
    results.appendChild(li);
});




// verbose version:
// function doTheMath(event){
//     let x = parseFloat(num1.value);
//     let y = parseFloat(num2.value);
//     let answer;
//     if (oper.value === '+') {
//         answer = x + y;
//     }
//     else if (oper.value === '-') {
//         answer = x - y;
//     }
//     else if (oper.value === '*') {
//         answer = x * y;
//     }
//     else if (oper.value === '/') {
//         answer = x / y;
//     }
//     let li = document.createElement("li");
//     li.innerText = answer;
//     results.appendChild(li);
// }

// btn.addEventListener('click', doTheMath);