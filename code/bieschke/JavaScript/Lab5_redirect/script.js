let sites = [
    'https://xkcd.com',
    'https://smbc-comics.com',
    'https://facebook.com',
    'https://instagram.com',
    'https://news.google.com',
    'https://onceuponatee.com',
    'https://smile.amazon.com',
];

let seconds = 5;

submit.addEventListener('click', function (timer) {

    setTimeout(timer(), 5000);

    function timer() {
        seconds -= 1;
        if (seconds = 0) {
            window.location = sites[Math.floor(Math.random() * sites.length)];
        } 
        // else {
        //     document.getElementById("timer").innerHTML = seconds;
        //     window.setTimeout("timer()", 1000);
        // }
    }

});


