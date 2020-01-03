let result = document.getElementById('result');
let result2 = document.getElementById('result2');
let result3 = document.getElementById('result3');
let list = document.getElementById('list');
let start = document.getElementById('start');
let lap = document.getElementById('lap');
let input = document.getElementById('input');
let startCount = document.getElementById('startCount');
let result4 = document.getElementById('result4');
let userUnit = document.getElementById('userUnit');
let stopWatch;

function newClock() {
    setInterval(function() {
        let d = new Date();
        result.innerText = d;
    }, 1000);
};

startCount.addEventListener('click', countDown);

function countDown() {

    let userInput = input.value;
    let inputType = userUnit.value;
    if (inputType == 'hours') {
        userInput = userInput * (1000 * 60 * 60);
    } else if (inputType == 'minutes') {
        userInput = userInput * (1000 * 60);
    } else if (inputType == 'seconds') {
        userInput = userInput * 1000;
    };

    let distance = userInput;

    setInterval(function() {
        distance = distance - 1000;
        console.log(userInput);
        console.log(distance);
        let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((distance % (1000 * 60)) / 1000);
        result4.innerText = hours + "h " + minutes + "m " + seconds + "s ";

        if (distance < 0) {
            result4.innerText = "Timer Expired";
        }
    }, 1000);
};



start.addEventListener('click', myStopWatch);

let timer = new Date();
timer.setHours(0, 0, 0, 0);
let lapTimer;

function myStopWatch() {
    setInterval(function() {
        timer.setSeconds(timer.getSeconds() + 1);
        result2.innerText = timer;
        lapTimer = timer;
    }, 1000);
};

lap.addEventListener('click', myLap);

function myLap() {
    console.log(lapTimer);
    let ol = document.querySelector('ol');
    let li = document.createElement('li');
    li.innerHTML = `<label>${lapTimer}</label>`;
    ol.appendChild(li);
};