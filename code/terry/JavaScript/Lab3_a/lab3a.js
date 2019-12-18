let aFoot = 0.3048;
let aMile = 1609.34;
let aMeter = 1.0;
let aKilo = 1000.0;
let aYard = 0.9144;
let anInch = 0.0254;

let userUnit;
let userOutput;
let userDistance;
let x;
let y;
let k;

userUnit = prompt('What is the unit input? From: ');
userOutput = prompt('What is the unit output? To: ');
userDistance = prompt('What is the distance to be converted? ');
userDistance = parseFloat(userDistance);
userOutput = userOutput.toLowerCase();
userUnit = userUnit.toLowerCase();

if (userUnit == userOutput) {
    alert('These units are the same.')
} else if (userDistance <= 0) {
    alert('Enter a number above zero.')
} else {
    if (userUnit == "mi") {
        x = aMile * userDistance;
    } else if (userUnit == "ft") {
        x = aFoot * userDistance;
    } else if (userUnit == "m") {
        x = aMeter * userDistance;
    } else if (userUnit == "km") {
        x = aKilo * userDistance;
    } else if (userUnit == "yd") {
        x = aYard * userDistance;
    } else if (userUnit == "in") {
        x = anInch * userDistance;
    }

    if (userOutput == "mi") {
        y = 0.000621;
    } else if (userOutput == "ft") {
        y = 3.281;
    } else if (userOutput == "m") {
        y = 1;
    } else if (userOutput == "km") {
        y = 0.001;
    } else if (userOutput == "yd") {
        y = 1.094;
    } else if (userOutput == "in") {
        y = 39.370;
    }

    k = x * y;
    k = k.toFixed(2);
    alert(`${userDistance} ${userUnit} to ${userOutput} is approx: ${k}`);
}