let result = document.getElementById('result');
let result2 = document.getElementById('result2');
let result3 = document.getElementById('result3');
let start = document.getElementById('start');
let lap = document.getElementById('lap');

setTimeout(myFunction, 0);

function myFunction() {
    setInterval(() => {
        let d = new Date();
        result.innerText = d;
    }, 1000);
};

let countTime;

start.addEventListener('click', myStart);

function myStart() {
    countTime = new Date().getTime();
    setInterval(() => {
        let newLap = Math.floor(new Date().getTime() - countTime);
        let seconds = Math.floor((newLap % (1000 * 60)) / 1000);
        result2.innerText = `Stopwatch Started.  Elasped Time: ${seconds}`;
    }, 1000);
};

lap.addEventListener('click', myLap);

function myLap() {
    let newLap = Math.floor(new Date().getTime() - countTime);
    let hours = Math.floor((newLap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((newLap % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((newLap % (1000 * 60)) / 1000);
    result3.innerText = `${hours} : ${minutes} : ${seconds}`;

    additem(`${hours} : ${minutes} : ${seconds}`);

    function additem(item) {
        let ol = document.querySelector('ol');
        let li = document.createElement('li');
        li.innerHTML = `<label>${item}</label>`;
        ol.appendChild(li);
    }
};