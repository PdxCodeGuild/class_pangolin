function clearClock() {
    var currentTime = new Date();
    currentTime.setHours(0,0,0,0);
    return currentTime;
}

function stopWatch() {
    currentHours = currentTime.getHours();
    currentMinutes = currentTime.getMinutes();
    currentSeconds = currentTime.getSeconds();

    currentHours = (currentHours < 10 ? "0" : "") + currentHours;
    currentMinutes = (currentMinutes < 10 ? "0" : "") + currentMinutes;
    currentSeconds = (currentSeconds <10 ? "0" : "") + currentSeconds;

    var currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds;

    var textField = document.getElementById("sw-time");
    textField.innerText = currentTimeString;

    console.log(currentTimeString);
    currentTime.setSeconds(currentTime.getSeconds() + 1);
    return currentTimeString;
}

// function saveTime() {

// }
let stopwatch_interval;
var currentTime = clearClock();
document.getElementById("sw-start").addEventListener("click", function() {
    currentTimeString = stopWatch();
    stopwatch_interval = setInterval(stopWatch, 1000)
});

document.getElementById("sw-reset").addEventListener("click", function() {
    currentTime = clearClock()
    document.getElementById("sw-time").innerText = "00:00:00"});

document.getElementById("sw-stop").addEventListener("click", function() {
    clearInterval(stopwatch_interval)});

document.getElementById("sw-save").addEventListener("click", function() {
    document.getElementsByTagName("")
    appendChild
})