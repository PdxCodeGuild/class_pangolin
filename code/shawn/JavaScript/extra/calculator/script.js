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

// number event listeners for buttons
button1.addEventListener('click', function () {
    result.value += "1";
});
button2.addEventListener('click', function () {
    result.value += "2";
});
button3.addEventListener('click', function () {
    result.value += "3";
});
button4.addEventListener('click', function () {
    result.value += "4";
});
button5.addEventListener('click', function () {
    result.value += "5";
});
button6.addEventListener('click', function () {
    result.value += "6";
});
button7.addEventListener('click', function () {
    result.value += "7";
});
button8.addEventListener('click', function () {
    result.value += "8";
});
button9.addEventListener('click', function () {
    result.value += "9";
});
button0.addEventListener('click', function () {
    result.value += "0";
});
// event listener for number keys
window.addEventListener('keydown', function (event) {
    console.log(event.code)
    if (event.code.toString().indexOf("Digit") != -1) {
        result.value += event.code.toString().slice(-1);
    }
});

