let message = document.getElementById("countdown");

let urls = [
    "https://brave.com/",
    "https://coinmarketcap.com/",
    "https://dragonchain.com/",
    "https://www.mentalfloss.com/article/63484/11-short-facts-about-corgis"
];

function redirect() {
    let url = urls[Math.floor(urls.length * Math.random())];
    window.location.assign(url);
};

function countDown4() {
    message.innerHTML = "You will be redirected in: 4";
};
function countDown3() {
    message.innerHTML = "You will be redirected in: 3";
};
function countDown2() {
    message.innerHTML = "You will be redirected in: 2";
};
function countDown1() {
    message.innerHTML = "You will be redirected in: 1";
};

setTimeout(countDown4, 1000);
setTimeout(countDown3, 2000);
setTimeout(countDown2, 3000);
setTimeout(countDown1, 4000);
setTimeout(redirect, 5000);