let operator = document.getElementById("operator");
let number1 = document.getElementById("number1");
let number2 = document.getElementById("number2");
let button = document.getElementById("calculator");
let results = document.getElementById("results");



// while (validInput) {

// }
function calculator() {

    let first_num = parseFloat(number1.value);
    let second_num = parseFloat(number2.value);
    let answer;

    // alert("Ok you would like to do "+ first_num + operation_type + second_num + ".");

    // let operation = operation_type;
    if (operator.value === '+') {
        answer = first_num + second_num;
    }   else if (operator.value === '-') {
        answer = first_num - second_num;
    }   else if (operator.value === '*') {
        answer = first_num * second_num;
    }   else if (operator.value === '/') {
        answer = first_num / second_num;
    }   else {
            alert('please enter a valid responce: ')
    }
    if (answer) {
        results.innerText = answer;
    }
}
button.addEventListener('click', calculator);

// console.log(answer);
    // let ul = document.createElement("ul");
    // ul.innerText = answer;
    // results.appendChild(ul);
// button.addEventListener('click')
