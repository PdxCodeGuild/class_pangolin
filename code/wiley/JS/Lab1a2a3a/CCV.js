/* 
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid. */


// get user card number input //
let cardNums = prompt("What is you credit card number. ");
console.log(cardNums);

//makes the string into an array //
let cardNumsArray = Array.from(cardNums);
console.log("Is this right? " + cardNumsArray);

//turns each item of the array into an integer//
let realCardNumsArray = []
for (let i = 0; i < cardNumsArray.length; i++) {
    realCardNumsArray.push(parseInt(cardNumsArray[i]));
}

// remove the last item of the array and save for later //

let checkNum = realCardNumsArray.pop();
console.log(checkNum);
console.log(realCardNumsArray);

//reverse the array//
let reversedArray = realCardNumsArray.reverse();
console.log(reversedArray);

// double every other item in the list //
function doubleEveryOther(x) {
    for (let i = 0; i < x.length; i += 2) {
        x[i] *= 2;
    }
    return x;
}
doubleEveryOther(reversedArray);
console.log("doubled every other " + reversedArray);

// subtract 9 from numbers over nine //

function subtractNine(x) {
    for (let i= 0; i < x.length; i++){
        if (x[i] > 9) {
            x[i] -= 9;
        }
    }
    return x;
}
subtractNine(reversedArray);
console.log(reversedArray);
 
// sum all the numbers in the list together //
function addUp(x) {
    return x.reduce(function(a,b) {
        return a + b
    }, 0);
}
let summed =addUp(reversedArray);
console.log(summed);

// take the second digit of the sum //
let numString = summed.toString();
console.log(numString);
numString = Array.from(numString);
console.log(numString);
finalCheck = numString[1];
console.log(finalCheck);

//check if the second digit matches the checked digit from before //

let verify = parseInt(finalCheck)
if (verify === checkNum) {
    document.write("Credit card verification passed! ");
} 
else {
    document.write("Verification Error. ")
}