function clock() {
    document.getElementById("clock").innerHTML = new Date();
}

setInterval(clock, 1000);