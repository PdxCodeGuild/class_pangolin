var timer = document.getElementById('timer');
var toggleBtn = document.getElementById('toggle');
var resetBtn = document.getElementById('reset');
var lapBtn = document.getElementById("lap");
var lapContainer = document.getElementById("laps");
// var lapTimes = document.getElementsByClassName('lapTimes');

var watch = new Stopwatch(timer);
var lapCounter = 0;
toggleBtn.addEventListener('click', function(){
    if (watch.isOn) {
        watch.stop();
        toggleBtn.textContent='Start'
    } else {
        watch.start();
        toggleBtn.textContent='Stop'
    }
});

resetBtn.addEventListener('click', function(){
    watch.reset();
    // var lapTimes = document.getElementsByClassName('lapTimes');
    var lapTimes = document.getElementById('laps').nodeType;
    console.log(lapTimes);
    lapTimes.forEach(element => {
        element.remove()
    });
    //need to figure out how to remove previous laps upon reset

});
lapBtn.addEventListener('click', function() {
    // watch.lap();
    lapCounter++;
    var lapTime = document.createElement('p');
    lapTime.classList.add("lapTimes");
    lapTime.innerText = `Lap ${lapCounter}  ${watch.lap()}`;
    lapContainer.appendChild(lapTime);
});