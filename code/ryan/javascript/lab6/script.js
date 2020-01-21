let clock = document.getElementById('clock');
let stopwatch = document.getElementById('stopwatch');
let stopwatchButton = document.getElementById('stopwatch-button');

setInterval(function(){
    let time = new Date();
    let hour = time.getHours();
    let minutes = time.getMinutes();
    let seconds = time.getSeconds();
    clock.innerHTML = hour + ":" + minutes + ":" + seconds;
})

// stopwatch


let startTime = new Date();
startTime.setHours(0,0,0,0);
stopwatch.innerHTML = startTime;

start.addEventListener('click', function () {

    count = setInterval(add, 1000);
  });
    




