let clock = setInterval(myClock, 1000);
let start = document.getElementById("start");
let stop = document.getElementById("stop");
let reset = document.getElementById("reset");

// clock
function myClock() {
  let d = new Date();
  document.getElementById("clock").innerHTML = d.toLocaleTimeString();
}

function add() {
  s.setSeconds(s.getSeconds() + 1)
  document.getElementById("stopwatch").innerHTML = s;
}

//stopwatch
let s = new Date();
s.setHours(0, 0, 0, 0);
document.getElementById("stopwatch").innerHTML = s;

start.addEventListener('click', function () {

  t = setInterval(add, 1000);
  //document.getElementById("stopwatch").innerHTML = s;
  console.log(s)
});

// stop stopwatch
stop.addEventListener('click', function () {
  clearInterval(t);
  document.getElementById("stopwatch").innerHTML = s;
  console.log(s)
});

// reset stopwatch
reset.addEventListener('click', function () {

  s.setHours(0, 0, 0, 0);
  document.getElementById("stopwatch").innerHTML = s;
  console.log(s)
});

