var urls = new Array();
urls[0] = 'https://explore.org/livecams/kitten-rescue/kitten-rescue-baby-kittens';
urls[1] = 'https://bestlifeonline.com/puppies-other-animals/';
urls[2] = 'https://www.boredpanda.com/cute-baby-elephants/?utm_source=googleutm_medium=organic&utm_campaign=organic';

var random = Math.floor(Math.random() * urls.length);

window.setTimeout(5000)

var seconds = 5;

function countdown() {
    seconds = seconds - 1;
    if (seconds < 0) {
        window.location = urls[random];
    } else {
        document.getElementById("countdown").innerHTML = seconds;
        window.setTimeout("countdown()", 1000);
    }
}

countdown();