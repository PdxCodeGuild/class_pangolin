// get DOM elements
let equation = document.getElementById("equation");
let result = document.getElementById("result");
let button1 = document.getElementById("button-1");
let button2 = document.getElementById("button-2");
let button3 = document.getElementById("button-3");
let button4 = document.getElementById("button-4");
let button5 = document.getElementById("button-5");
let button6 = document.getElementById("button-6");
let button7 = document.getElementById("button-7");
let button8 = document.getElementById("button-8");
let button9 = document.getElementById("button-9");
let button0 = document.getElementById("button-0");
let buttonDecimal = document.getElementById("button-decimal");
let buttonAdd = document.getElementById("button-add");
let buttonSubtract = document.getElementById("button-subtract");
let buttonMultiply = document.getElementById("button-multiply");
let buttonDivide = document.getElementById("button-divide");
let buttonEqual = document.getElementById("button-equal");
let buttonFactorial = document.getElementById("button-factorial");
let buttonNegate = document.getElementById("button-negate");
let buttonExponent = document.getElementById("button-exponent");
let buttonSqrt = document.getElementById("button-sqrt");
let buttonModulus = document.getElementById("button-modulus");
let buttonSin = document.getElementById("button-sin");
let buttonCos = document.getElementById("button-cos");
let buttonTan = document.getElementById("button-tan");
let buttonClear = document.getElementById("button-clear");
let buttonBackspace = document.getElementById("button-backspace");

// array for holding numbers and operations 
let runningTotal = 0;
let numbers = [];
let isResult = true;
let mode = "numberOrOperator";
let activeOperation = '';

// number event listeners: mouse
let numButtons = document.getElementsByClassName("num-button");
for (let button of numButtons){
    button.addEventListener("click", function(){
        if (isResult) {
            result.innerText = this.innerText;
            isResult = false;
        } else {
            result.innerText += this.innerText;
        }
    });
}

// number event listener: keyboard
window.addEventListener('keydown', function (event) {
    if (event.code.toString().indexOf("Digit") != -1) {
        let dig = event.code.toString().slice(-1);
        if (isResult) {
            result.innerText = dig.toString();
            isResult = false;
        } else {
            result.innerText += dig.toString();
        }
    }
});

// operations event listeners
buttonAdd.addEventListener('click', function () {
    // set addition to active operation
    activeOperation = "+";

    // if a non-result is showing, do math
    if (!isResult) {
        numbers.push(" + ");
        updateEquation();
        doMath();
    } else {
        numbers.pop();
        numbers.push(" + ");
        updateEquation();
    }
});
// operations event listeners
buttonSubtract.addEventListener('click', function () {
    // set addition to active operation
    activeOperation = "-";

    // if a non-result is showing, do math
    if (!isResult) {
        numbers.push(" - ");
        updateEquation();
        doMath();
    } else {
        numbers.pop();
        numbers.push(" - ");
        updateEquation();
    }
});
// operations event listeners
buttonEqual.addEventListener('click', function () {
    // set addition to active operation
    doMath(true);
});
// non-math operations event listeners
buttonClear.addEventListener('click', function () {
    numbers = [];
    result.innerText = '';
    equation.innerText = '';
    runningTotal = 0;
    updateEquation();
});
buttonBackspace.addEventListener('click', function () {
    result.innerText = '';
});


function updateEquation() {
    equation.innerText = '';
    for (let num of numbers) {
        equation.innerText += num.toString();
    }
}

function doMath(isFinal = false) {


    // get working number, push to numbers array
    let workingNumber = parseFloat(result.innerText);
    numbers.push(workingNumber);


    // do math assuming equal sign not pressed
    if (!isFinal) {
        if (activeOperation === "+") {

            result.innerText = (parseFloat(runningTotal) + workingNumber).toString();
        }
        else if (activeOperation === "-") {
            result.innerText = (parseFloat(runningTotal) - workingNumber).toString();
        }
        else if (activeOperation === "*") {
            numbers.push(" × ");
            result.innerText = (parseFloat(runningTotal) * workingNumber).toString();
        }
        else if (activeOperation === "/") {
            numbers.push(" ÷ ");
            result.innerText = (parseFloat(runningTotal) / workingNumber).toString();
        }
        // update running equation
        updateEquation();
    } else {
        numbers.push(" = ");
        let finalResult;
        if (activeOperation === "+") {
            finalResult = (parseFloat(runningTotal) + workingNumber).toString();
        }
        else if (activeOperation === "-") {
            finalResult = (parseFloat(runningTotal) - workingNumber).toString();
        }
        else if (activeOperation === "*") {
            finalResult = (parseFloat(runningTotal) * workingNumber).toString();
        }
        else if (activeOperation === "/") {
            finalResult = (parseFloat(runningTotal) / workingNumber).toString();
        }
        result.innerText = finalResult;
        numbers.push(finalResult);
        // update running equation
        updateEquation();
        numbers = [finalResult];
    }

    // update result bool and runningTotal
    isResult = true;
    runningTotal = result.innerText;
}
