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

// new list of iframe friendly websites?

// get a reference to the redirect button
let redirectButton = document.getElementById('redirect');
let iframe = document.getElementById('myiframe');
// let iframe = document.getElementsByTagName('iframe')[0];
let nextSiteButton = document.getElementById('next-site-button');

// countdown counter
let countdown = 4;

// function for updating button text
function tick(){
    redirectButton.innerText = `redirecting in ${countdown} sec...`;
    countdown--;
    if (countdown === 0){
        // pick random URL
        let randomUrl = urls[Math.floor(Math.random()*urls.length)]
        location = randomUrl;
    }
}

// add click event listener to trigger redirect
redirectButton.addEventListener('click', function(){
    // pick random URL
    let randomUrl = urls[Math.floor(Math.random()*urls.length)]
    location = randomUrl;
});

// UNCOMMENT THIS TO ENABLE 5 SEC AUTO REDIRECT
// window.setInterval(tick, 1000);
nextSiteButton.addEventListener('click', function(){
    // pick random URL
    let randomUrl = urls[Math.floor(Math.random()*urls.length)]
    nextSiteButton.innerHTML = `You are at <strong>${randomUrl}</strong>....click for next site!`
    iframe.src = randomUrl;
});
