let aFoot = 0.3048;
let aMile = 1609.34;
let aMeter = 1.0;
let aKilo = 1000.0;
let aYard = 0.9144;
let anInch = 0.0254;

let submit = document.getElementById("submit");
let results = document.getElementById("results");
let form = document.getElementById("myForm");

let userUnit = document.getElementById("userUnit");
// let user_input = userUnit.value;
let userOutput = document.getElementById("userOutput");
// let user_output = userOutput.value;
let userDistance = document.getElementById("userDistance");
let x;
let y;
let k;

submit.addEventListener('click', function() {
    let user_input = userUnit.value;
    let user_output = userOutput.value;
    let user_distance = userDistance.value;

    console.log(user_distance);

    if (user_input == user_output) {
        results.innerText = 'These units are the same.';
    } else if (user_distance <= 0) {
        results.innerText = 'Enter a number above zero.';
    } else {
        if (user_input == "mi") {
            x = aMile * user_distance;
        } else if (user_input == "ft") {
            x = aFoot * user_distance;
        } else if (user_input == "m") {
            x = aMeter * user_distance;
        } else if (user_input == "km") {
            x = aKilo * user_distance;
        } else if (user_input == "yd") {
            x = aYard * user_distance;
        } else if (user_input == "in") {
            x = anInch * user_distance;
        }

        if (user_output == "mi") {
            y = 0.000621;
        } else if (user_output == "ft") {
            y = 3.281;
        } else if (user_output == "m") {
            y = 1;
        } else if (user_output == "km") {
            y = 0.001;
        } else if (user_output == "yd") {
            y = 1.094;
        } else if (user_output == "in") {
            y = 39.370;
        }

        k = x * y;
        k = k.toFixed(2);
        results.innerText = `${user_distance} ${user_input} to ${user_output} is approx: ${k}`;
    }
});