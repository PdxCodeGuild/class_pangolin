let numDiv = document.getElementById('number');
let submit = document.getElementById('submit');
let answer = document.getElementById('answer');
let ones_to_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
let tens_to_word = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
let teens_to_word = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];

function calculate() {
    num = parseInt(numDiv.value);
    let tens = Math.floor(num/10);
    let ones = num % 10;
    let result;
    if (num === 0) {
        result = 'zero';
    } else if (0<num && num<10) {
        result = ones_to_word[num-1];
    } else if (10<num && num<20) {
        result = teens_to_word[ones-1];
    } else {
        if (ones > 0) {
            result = tens_to_word[tens-1] + '-' + ones_to_word[ones-1];
        } else {
            result = tens_to_word[tens-1];
        } 
    }  
    if (result) {
        answer.innerText = "Your word is:  " + result;
    }    
}

submit.addEventListener('click', calculate);