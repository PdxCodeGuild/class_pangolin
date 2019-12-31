class Stopwatch {
    constructor(elem) {
        var time = 0;
        var interval;
        var offset;
        this.isOn = false;
        function update() {
            if (this.isOn) {
                time += delta();
            }
            var formattedTime = timeFormatter(time);
            elem.textContent = formattedTime;
        }
        ;
        function delta() {
            var now = Date.now();
            var timePassed = now - offset;
            offset = now;
            return timePassed;
        }
        ;
        function timeFormatter(timeInMilliseconds) {
            var time = new Date(timeInMilliseconds);
            var minutes = time.getMinutes().toString();
            var seconds = time.getSeconds().toString();
            var milliseconds = time.getMilliseconds().toString();
            if (minutes.length < 2) {
                minutes = '0' + minutes;
            }
            if (seconds.length < 2) {
                seconds = '0' + seconds;
            }
            while (milliseconds.length < 3) {
                milliseconds = '0' + milliseconds;
            }
            return minutes + ':' + seconds + '.' + milliseconds;
        }
        ;
        this.start = function () {
            if (!this.isON) {
                interval = setInterval(update.bind(this), 10);
                offset = Date.now();
                this.isOn = true;
                }
        }
        ;
        this.stop = function () {
            if (this.isOn) {
                clearInterval(interval);
                interval = null;
                this.isOn = false;
                }
        }
        ;
        this.reset = function () {
            if (!this.isOn){
                console.log("test")
                time = 0;
                update();
            }
        };
        this.lap = function () { };
    }
}
;
var watch = new Stopwatch();

// var time = document.getElementById('timer');
// var toggleBtn = document.getElementById('toggle');
// var resetBtn = document.getElementById('reset');
// var watch = new Stopwatch();

// toggleBtn.addEventListener('click', function(){
//     if (watch.isOn) {
//         watch.stop();
//     } else {
//         watch.start();
//     }
// });

// resetBtn.addEventListener('click', function(){
//     watch.reset();
// });
// console.log("hi");