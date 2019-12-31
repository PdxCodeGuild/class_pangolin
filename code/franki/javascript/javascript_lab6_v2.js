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
    textField.innerHTML = currentTimeString;

    console.log(currentTimeString)

    currentTime.setSeconds(currentTime.getSeconds() + 1);
}

var currentTime = clearClock();
document.getElementById("sw-start").addEventListener("click", function() {
    stopWatch();
    setInterval(stopWatch, 1000)
});

document.getElementById("sw-reset").addEventListener("click", clearClock()
);

document.getElementById("sw-stop").addEventListener("click", clearInterval(stopWatch));