var sw = {
    // [INIT]
    etime: null, // Holds time display
    erst: null, // Holds reset button
    ego: null, // Holds start/stop button
    elap: null, // Holds lap button
    timer: null, // Timer object
    now: 0,
    lastLap: document.getElementById('laps'), // Lap times

    init: function() {
        // Get HTML elements
        sw.etime = document.getElementById('sw-time');
        sw.erst = document.getElementById('sw-rst');
        sw.ego = document.getElementById('sw-go');
        sw.elap = document.getElementById('sw-lap');

        // Attach listeners
        sw.erst.addEventListener('click', sw.reset);
        sw.erst.disabled = false;
        sw.ego.addEventListener('click', sw.start);
        sw.ego.disabled = false;
        sw.elap.addEventListener('click', sw.lap);
        sw.elap.disabled = false;
    },
    tick: function() {
        // Update display if stopwatch is running
        sw.now++;
        var remain = sw.now;
        var hours = Math.floor(remain / 3600);
        remain -= hours * 3600;
        var mins = Math.floor(remain / 60);
        remain -= mins * 60;
        var secs = remain;

        // Update display timer
        if (hours < 10) {
            hours = '0' + hours;
        }
        if (mins < 10) {
            mins = '0' + mins;
        }
        if (secs < 10) {
            secs = '0' + secs;
        }
        sw.etime.innerHTML = hours + ':' + mins + ':' + secs;
    },
    start: function() {
        // Start stopwatch
        sw.timer = setInterval(sw.tick, 1000);
        sw.ego.value = 'Stop';
        sw.ego.removeEventListener('click', sw.start);
        sw.ego.addEventListener('click', sw.stop);
    },

    stop: function() {
        // Stop stopwatch
        clearInterval(sw.timer);
        sw.timer = null;
        sw.ego.value = 'Start';
        sw.ego.removeEventListener('click', sw.stop);
        sw.ego.addEventListener('click', sw.start);
        console.log("stop")
    },

    reset: function() {
        // Stop first if running
        if (sw.timer != null) {
            sw.stop();
        }
        // Reset
        sw.now = -1;
        sw.tick();
    },
    // d.setHours(0, 0, 0, 0); 
    lap: function() {
        let d = new Date();
        const options = {
            timeZone: 'America/Los_Angeles',
            hours12: true,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
        }
        let n = d.toLocaleDateString('en-US', options);
        let li = document.createElement('li');
        console.log('li');
        li.innerText = n;
        sw.lastLap.appendChild(li);
    },


    // lap: function() {
    //     let d = new Date();
    //     let options = {
    //         month: '2-digit',
    //         day: '2-digit',
    //         year: '2-digit',
    //         hour: '2-digit',
    //         minute: '2-digit',
    //         second: '2-digit',
    //     }
    //     console.log(d.toLocaleTimeString('eng-us', options));
    //     let li = document.createElement('li');
    //     console.log('li');
    //     li.innerText = d;
    //     sw.lastLap.appendChild(li);
    // },


};

window.addEventListener('load', sw.init);