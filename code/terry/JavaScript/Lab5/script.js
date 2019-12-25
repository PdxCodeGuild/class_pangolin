let submit = document.getElementById('submit');

let urlArray = ['https://www.google.com', 'https://www.hotmail.com', 'https://www.gmail.com'];

let rand = urlArray[(Math.random() * urlArray.length) | 0];

submit.addEventListener('click', function() {
    // console.log(rand);
    // myFunction();
    time = 5, r = document.getElementById('result'), tmp = time;

    setInterval(function() {
        var c = tmp--,
            m = (c / 60) >> 0,
            s = (c - m * 60) + '';
        if (s == 1) {
            location.replace(rand);
        } else {
            console.log(s);
            r.textContent = 'Page redirect in ' + (s.length > 1 ? '' : '0') + s
            tmp != 0 || (tmp = time);
        }
    }, 1000);
});