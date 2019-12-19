let numbers = [5, 0, 8, 3, 4, 1, 6];

let sum = numbers.reduce(myFun);

function myFun(total, value, index, array) {
    return total + value;
}

alert('Version 1 of the Average Numbers Lab');

alert(sum);

let outPut;

outPut = sum / numbers.length;

alert(outPut);

let rounded;

rounded = outPut.toFixed(2);

alert(rounded);

alert('Version 2 of the Average Numbers Lab');

let numbers2 = [];
let userInput = "";
let outPut2 = 0;
let outPut3 = 0;
let finish = true;

while (finish) {
    userInput = prompt('Please enter a number or "Done" to finish. ');
    if (userInput.toLowerCase() == "done") {
        finish = false;
    } else {
        numbers2.push(userInput);
        // console.log(numbers2);
        outPut2 += parseInt(userInput);
        // console.log(outPut2);
        // console.log(numbers2);
    }

}

let len;

len = numbers2.length;
// console.log(len);

outPut3 = outPut2 / len;
// console.log(outPut3);

let rounded2;

rounded2 = outPut3.toFixed(2);

alert(rounded2);