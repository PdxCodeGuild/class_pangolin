let urls = ['https://en.wikipedia.org/wiki/Satire', 'https://www.youtube.com/results?search_query=javascript+tutorial+redirect', 'https://github.com/PdxCodeGuild/class_pangolin/blob/master/4%20JavaScript/labs/lab05-random_redirector.md', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random']

function randomRedirect() {
    min = 0;
    max = urls.length;
    index = Math.random() * (max - min) + min;
    console.log(index);
    console.log(urls[index]);
    url = urls[index];
    window.location.assign(url);
};

// document.getElementById("button").addEventListener("click", function() {
//     randomRedirect()});