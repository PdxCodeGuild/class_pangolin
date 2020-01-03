let timeMeow = document.getElementById('timeMeow');
let stopwatch = document.getElementById('stopwatch');
let lapTime = document.getElementById('lapTime');
let startBtn = document.getElementById('startBtn');
let lapBtn = document.getElementById('lapBtn');

function showEpoc(){
    setInterval(() =>{
        let dateInit = new Date()
        let epoc = dateInit.getTime()/1000;
        timeMeow.innerText = epoc;
    })
};

function startTimerMeow() {
    startTime = new Date().getTime()/1000;
    setInterval(() => {
        let beginTime = new Date().getTime()/1000 - startTime;
        stopwatch.innerText = beginTime;
    })
};

function testPrinter() {
    let lapTimeMeow = stopwatch.innerText
    let ol = document.querySelector('ol');
    let li = document.createElement('li');
    li.innerHTML = `<label>${lapTimeMeow}</label>`;
    ol.appendChild(li);
};

showEpoc();
startBtn.addEventListener('click', startTimerMeow);
lapBtn.addEventListener('click', testPrinter);
