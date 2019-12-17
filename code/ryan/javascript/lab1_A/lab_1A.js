let operators = ['+', '-', '*', '/'];
alert('This is a calculator.  You will enter the first number, the operation desired, and finally the second number!');

let first = parseInt(prompt('What is your first number?'));
let operation = prompt('What is the operation you would like to perform?  (+, -, *, /)');
let second = parseInt(prompt('What is your second number?'));

let calculations = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
};

if (operation === '+') {
    result = calculations.add(first, second);
} else if (operation === '-') {
    result = calculations.subtract(first, second);
} else if (operation === '*') {
    result = (calculations.multiply(first, second));
} else {
    result = (calculations.divide(first, second));
}

alert('Your result is:  ' + result);