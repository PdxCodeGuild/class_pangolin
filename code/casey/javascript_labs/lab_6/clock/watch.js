let startBtn = document.getElementById("start");
let watch = document.getElementById("watch");
let d = new Date();

startBtn.addEventListener("click", function(e) {
    watch.innerHTML = d.setHours(0,0,0,0);
});

function stopWatch() {
    watch.innerHTML = new Date().setHours(0,0,0,0);
}

setInterval(stopWatch, 1000);
