//TEST CCNUMBER IS 4556737586899855 //
let checkNum;
let returnObject = document.getElementById("return");
let cardNumsRaw;
function convertstring(){
    //makes the string into an array //
    cardNumsRaw = document.getElementById("user-number");
    let cardNums = cardNumsRaw.value; 
    console.log(cardNums);
    let cardNumsArray = Array.from(cardNums);
    console.log("Is this right? " + cardNumsArray);

    //turns each item of the array into an integer//
    let realCardNumsArray = []
    
    for (let i = 0; i < cardNumsArray.length; i++) {
        if (isNaN(parseInt(cardNumsArray[i])) === true){
            return returnObject.innerText = "A non-number detected. Make sure your credit card number contains no letters or spaces."
        };
        realCardNumsArray.push(parseInt(cardNumsArray[i]));
    }
    
    // remove the last item of the array and save for later //
    checkNum = realCardNumsArray.pop();
    console.log(checkNum);
    console.log(realCardNumsArray);

    //reverse the array//
    let reversedArray = realCardNumsArray.reverse();
    console.log(reversedArray);
    return reversedArray;
};


// double every other item in the list //
function doubleEveryOther(x) {
    for (let i = 0; i < x.length; i += 2) {
        x[i] *= 2;
    }
    return x;
};

function subtractNine(x) {
    for (let i= 0; i < x.length; i++){
        if (x[i] > 9) {
            x[i] -= 9;
        }
    }
    return x;
};

// sum all the numbers in the list together //
function addUp(x) {
    return x.reduce(function(a,b) {
        return a + b
    }, 0);
};

function getSecondAndCheck(x){
    numString = x.toString();
    numString = Array.from(numString);
    console.log(numString);
    finalCheck = numString[1];
    console.log(finalCheck);
    let verify = parseInt(finalCheck);
    returnObject = document.getElementById("return");
    if (verify === checkNum) {
        
        returnObject.innerText = "Credit card verification passed!";
    }
    else {

        returnObject.innerText = "Verification Error. Possible Invalid Credit Card. ";
    }
    
};

function validator() {
     return getSecondAndCheck(addUp(subtractNine(doubleEveryOther(convertstring()))));
}
function clean() {
    cardNumsRaw = document.getElementById("user-number");
    return cardNumsRaw.value = null;

}
let validate = document.getElementById("submit-btn");
validate.addEventListener("click", validator);
let another = document.getElementById("another");
another.addEventListener("click", clean);