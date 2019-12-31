let countdown = document.querySelector('#countdown');
let c = 5;
let urls = [
    'https://truefire.com/online-guitar-lessons/',
    'https://www.youtube.com/',
    'https://www.google.com/'
];

setInterval(function(){
    countdown.innerText = c;
    if (c === 0){
        let redirect = urls[Math.floor(Math.random() * urls.length)];
        window.location = redirect;
    }
    c--;
}, 1000);