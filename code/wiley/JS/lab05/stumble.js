/* Creating a basic Stumble Upon clone.  Using an i.frame element to display a random webpage inside the homepage.  
Version 2, give a count down before reloading page.  */

//TODO: 1) get the iframe to load on button click, only once.  aka start stumble button
// 2) upon clicking the start stumble button, iframe is created along with arrow button to keep stumbling
// 3) arrow click function brings new load to iframe
// 4) timer that displays 5 second count down for some reason (version 2 requirement) (JS timing-events)
// 5) style (bootstrap?)


/* comment to test window objects 
let nextBtn = document.getElementById("next");
let stumbleWindow = document.createElement("iframe");
stumbleWindow.setAttribute("id","stumbleWindow");
let frameSpot = document.getElementById("frameSpot");
frameSpot.appendChild(stumbleWindow);
stumbleWindow.style.display="none";
let webList = ["https://en.wikipedia.org/wiki/Special:Random","https://www.youtube.com","https://www.reddit.com","https://www.wileyrummel.com"];
let randomSite = webList[Math.floor(Math.random() * webList.length)];
console.log(randomSite);
let showlocation = document.getElementById("locationdisplay")


stumbleWindow.setAttribute("width","100%");
stumbleWindow.setAttribute("height", "90%");
nextBtn.addEventListener("click", function(){
    console.log("test");
    stumbleWindow.style.display="block";
    stumbleWindow = document.getElementById("stumbleWindow");
    // stumbleWindow.src=webList[Math.floor(Math.random() * webList.length)];
    console.log(stumbleWindow.src)
    stumbleWindow.setAttribute("src","https://en.wikipedia.org/wiki/Special:Random");
    showlocation.innerText = stumbleWindow.location.href;
});
*/
console.log(window.location)
var x = window.location
// x.assign("http://www.wikipedia.org")
let webString = ["https://en.wikipedia.org/wiki/Horten_H.V","https://en.wikipedia.org/wiki/Laurie_Barnett","https://en.wikipedia.org/wiki/Danny_Kallis","https://en.wikipedia.org/wiki/Tabunia","https://en.wikipedia.org/wiki/List_of_national_parks_of_the_Dominican_Republic"];
let randomSite = webString[Math.floor(Math.random() * webString.length)];
x.assign(randomSite);