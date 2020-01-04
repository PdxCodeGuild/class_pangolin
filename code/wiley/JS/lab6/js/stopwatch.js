class Stopwatch {
    constructor(elem) {
        var time = 0;
        var interval;
        var offset;
        var isOn = false;
        // var lapCounter = 0;

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
            var time = new Date(timeInMilliseconds); //ex 1
            // var time = Date.now(timeInMilliseconds); // ex 2
            // var hours = (time/3600000).toString(); // ex 2
            // var minutes = (time/60000).toString(); // ex 2
            // var seconds = (time/1000).toString(); // ex 2
            // var milliseconds = time.toString(); // ex 2
            var hours = time.getHours();//ex 1
            console.log(hours);//ex 1
            hours-= 16//ex 1
            hours.toString();//ex 1
            var minutes = time.getMinutes().toString();//ex 1
            var seconds = time.getSeconds().toString();//ex 1
            var milliseconds = time.getMilliseconds().toString();//ex 1
            if (hours.length < 2) {
                hours = '0' + hours;
            }
            if (minutes.length < 2) {
                minutes = '0' + minutes;
            }
            if (seconds.length < 2) {
                seconds = '0' + seconds;
            }
            while (milliseconds.length < 3) {
                milliseconds = '0' + milliseconds;
            }
 
            return hours+ ':' + minutes + ':' + seconds + '.' + milliseconds;
        }
        ;
        this.start = function () {
            if (!this.isON) {
                interval = setInterval(update.bind(this), 1);
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
                time = 0;
                // update(); using update function throws an error that if (this.isOn) is undefined.  
                var formattedTime = timeFormatter(time);
                elem.textContent = formattedTime
            }
        };
        this.lap = function () {
            console.log(timeFormatter(time));
            return timeFormatter(time);
         };
    }
}
;
var watch = new Stopwatch();

