console.log(new Date());
let clock = document.getElementById("clock");
var myVar = setInterval(myTime, 1000),
    start = document.getElementById('start'),
    stop = document.getElementById('stop'),
    clear = document.getElementById('clear'),
    seconds = 0, minutes= 0, hours = 0;
    counter = document.getElementById('counter');

function myTime() {
    var d = new Date();
    clock.innerHTML = d.toLocaleString();
}
function add() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes=0;
            hours++;
        }
    }
    counter.textContent = (hours ? (hours >9 ? hours: "0" + hours):"00")+ ":" + (minutes ? (mintes> 9 ?minutes: "0" +minutes) : "00") + ":" + (seconds>9 ? seconds:"0" + seconds);
        timer();
}