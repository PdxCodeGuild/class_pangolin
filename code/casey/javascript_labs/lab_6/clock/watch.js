let watch = document.getElementById("watch");
let start = document.getElementById("start");
let stop = document.getElementById("stop");
let reset = document.getElementById("reset");
let laps = document.getElementById("laps");

let tic;

function sWatch() {
    h = d.getHours();
    m = d.getMinutes();
    s = d.getSeconds();

    h = (h < 10 ? "0" : "") + h;
    m = (m < 10 ? "0" : "") + m;
    s = (s < 10 ? "0" : "") + s;

    let display = h + ":" + m + ":" + s;
    watch.innerHTML = display;

    d.setSeconds(d.getSeconds() + 1);
};

function resetWatch() {
    let d = new Date();
    d.setHours(0,0,0,0);
    return d
};

let d = resetWatch();

start.addEventListener("click", function(e) {
    display = sWatch();
    tic = setInterval(sWatch, 1000);
});

stop.addEventListener("click", function(e) {
    clearInterval(tic);
});

reset.addEventListener("click", function(e) {
    d = resetWatch();
    watch.innerHTML = "00:00:00";
});

