// array of urls
let urls = [
    'https://www.google.com',
    'http://www.reddit.com',
    'http://www.facebook.com',
    'http://www.hulu.com',
    'http://www.netflix.com',
    'http://www.shawnstolsig.com',
    'http://www.linkedin.com',
    'http://www.worldofwarships.com',
    'http://www.youtube.com',
    'http://en.wikipedia.org',
    'http://www.twitter.com',
    'http://www.amazon.com',
    'http://www.imdb.com',
    'http://www.pintrest.com',
    'http://www.ebay.com',
    'http://www.tripadvisor.com',
    'http://www.walmart.com',
    'http://www.instagram.com',
    'http://www.apple.com',
    'http://www.nytimes.com',
    'http://www.indeed.com',
    'http://www.espn.com',
];
// urls that are iframe friendly for version3 
let iframeUrls = [
    'http://www.shawnstolsig.com',
    'http://en.wikipedia.org',
    'http://www.indeed.com',
    'https://en.wikipedia.org/wiki/After_the_Deluge_(painting)m',
    'https://en.wikipedia.org/wiki/Lord,_I_Apologize',
    'https://en.wikipedia.org/wiki/Yarabad_Mirbeyg',
    'https://en.wikipedia.org/wiki/Faramarz_Kola',
    'https://en.wikipedia.org/wiki/Nina_H%C3%B8iberg',
    'https://en.wikipedia.org/wiki/AC_Hotels',
    'https://en.wikipedia.org/wiki/Donald_Trump',
    'https://en.wikipedia.org/wiki/Miss_Universe',
    'https://en.wikipedia.org/wiki/Beidazoon',
];

// new list of iframe friendly websites?

// get references to DOM elements
let countdownEnabledRadio = document.getElementById("countdown-enabled");
let countdownDisabledRadio = document.getElementById("countdown-disabled");
let redirectButton = document.getElementById('redirect');
let redirectCountdown = document.getElementById('redirect-countdown');
let iframe = document.getElementById('myiframe');
let nextSiteButton = document.getElementById('next-site-button');

// add click event listener to trigger redirect
redirectButton.addEventListener('click', function(){
    // pick random URL
    let randomUrl = urls[Math.floor(Math.random()*urls.length)]
    location = randomUrl;
});

// countdown counter
let countdown = 5;

// function for updating button text
function tick(){
    countdown--;
    redirectCountdown.innerText = `redirecting in ${countdown} sec...`;
    if (countdown === 0){
        // pick random URL
        let randomUrl = urls[Math.floor(Math.random()*urls.length)]
        location = randomUrl;
    }
}
// assign setInterval to variable so that it can be stopped
let si;

// event listener for redirect countdown radio buttons
countdownDisabledRadio.addEventListener('click', function(){
    if (checkRadioButtons()){
        redirectCountdown.classList.remove("not-counting");
        redirectCountdown.classList.add('counting')
        redirectCountdown.innerText = `redirecting in ${countdown} sec...`;
        si = window.setInterval(tick, 1000);
    } else {
        clearInterval(si)
        countdown = 5;
        redirectCountdown.innerText = "countdown disabled"
        redirectCountdown.classList.remove('counting');
        redirectCountdown.classList.add("not-counting");
    }
});
countdownEnabledRadio.addEventListener('click', function(){
    if (checkRadioButtons()){
        redirectCountdown.classList.remove("not-counting");
        redirectCountdown.classList.add('counting')
        redirectCountdown.innerText = `redirecting in ${countdown} sec...`;
        si = window.setInterval(tick, 1000);
    } else {
        clearInterval(si)
        countdown = 5;
        redirectCountdown.innerText = "countdown disabled"
        redirectCountdown.classList.remove('counting');
        redirectCountdown.classList.add("not-counting");
    }
});
function checkRadioButtons(){
    return countdownEnabledRadio.checked;
};

// event listener for v3 taking user to next site
nextSiteButton.addEventListener('click', function(){
    // pick random URL
    let randomUrl = iframeUrls[Math.floor(Math.random()*iframeUrls.length)]
    nextSiteButton.innerHTML = `You are at <strong>${randomUrl}</strong>....click for next site!`
    iframe.src = randomUrl;
});

