let numbers2 = [];
let userInput = document.getElementById("userInput");
let outPut2 = 0;
let outPut3 = 0;
let submit = document.getElementById("submit");
let results = document.getElementById("results");
let form = document.getElementById("myForm");
let len;

submit.addEventListener('click', function() {
    let avgNum = userInput.value;
    //console.log(avgNum);
    if (avgNum == '') {
        results.innerText = 'You must enter a number.';
    } else {
        numbers2.push(avgNum);
        //console.log(numbers2);
        outPut2 += parseInt(avgNum);
        //console.log(outPut2);
        //console.log(numbers2);

        len = numbers2.length;
        //console.log(len);
        outPut3 = outPut2 / len;
        //console.log(outPut3);
        let rounded2;
        rounded2 = outPut3.toFixed(2);
        //console.log(rounded2);
        results.innerText = `The Average is: ${rounded2}`;
        form.reset();
    }
});