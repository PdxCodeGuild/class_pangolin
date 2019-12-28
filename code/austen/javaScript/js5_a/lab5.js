let find = document.getElementById("find");
let stationary = document.getElementById("stationary");
let stop = document.getElementById("stop");
let inline = document.getElementById("inlineFrame").style.display = "none";
let browse = document.getElementById("browse");

//iframe links
let iframe= [
    "https://wiki.python.org/moin/",
    "https://code.djangoproject.com/wiki",
    "https://en.wikipedia.org/wiki/HTML5",
    "https://en.wikipedia.org/wiki/JavaScript",
    "https://en.wikipedia.org/wiki/JSON",
    "https://en.wikipedia.org/wiki/JScript_.NET"
]
//links for page flipping
let arr = ["http://youtube.com","http://facebook.com",
"http://twitter.com","http://amazon.com",
"http://reddit.com","http://pinterest.com",
"http://ebay.com","http://walmart.com",
"http://instagram.com","http://nytimes.com",
"http://linkedin.com","http://indeed.com"
];
// function to redirect to different sites 
find.addEventListener('click', function(e){
    e.preventDefault();
//find the new url
    let newval = arr[Math.floor(Math.random() * arr.length)];
    // console.log(newval);
    let seconds = 6;
    let interval = setInterval(function(){
        document.getElementById("target").innerHTML = --seconds;

        if (seconds<= 1){
            document.getElementById("target").innerHTML = "Hold on tight!!";
            // clearInterval(interval)
            window.location.assign(newval);
            ;
        }
    }, 1000);
    
    stop.addEventListener('click', function(){
        clearInterval(interval);
    });
});


// alert("what is your birthday")
//version 3 implimenting iframe
browse.addEventListener('click', function(e){
    e.preventDefault();
    let newIframe = iframe[Math.floor(Math.random() * iframe.length)];
    console.log(newIframe);
    document.getElementById("inlineFrame").src = newIframe;
    document.getElementById("inlineFrame").style.display = "block";
});
