//Creating a basic Stumble Upon clone.  Using an i.frame element to display a random webpage inside the homepage.
//Version 2, give a count down before reloading page.  */

//TODO: 1) get the iframe to load on button click, only once.  aka start stumble button
// 2) upon clicking the start stumble button, iframe is created along with arrow button to keep stumbling
// 3) arrow click function brings new load to iframe
// 4) timer that displays 5 second count down for some reason (version 2 requirement) (JS timing-events)
// 5) style (bootstrap?)

//comment to test window objects
let nextBtn = document.getElementById("next");
let stumbleWindow = document.createElement("iframe");

stumbleWindow.setAttribute("id", "stumbleWindow");

let frameSpot = document.getElementById("frameSpot");
frameSpot.appendChild(stumbleWindow);

stumbleWindow.style.display = "none";

let webList = [
  "https://en.wikipedia.org/wiki/Special:Random",
  "https://en.wikipedia.org/wiki/Indonesia_national_rugby_sevens_team",
  "https://en.wikipedia.org/wiki/Myrcha",
  "https://en.wikipedia.org/wiki/Dickabram_Bridge",
  "https://en.wikipedia.org/wiki/Division_No._7,_Alberta"
];
function randomSite() {
    let myVar = webList[Math.floor(Math.random() * webList.length)];
    return myVar
}


console.log(randomSite());
// let showlocation = document.getElementById("locationdisplay");

stumbleWindow.setAttribute("width", "100%");
stumbleWindow.setAttribute("height", "90%");
nextBtn.addEventListener("click", function() {
  stumbleWindow.style.display = "block";
  stumbleWindow = document.getElementById("stumbleWindow");

  stumbleWindow.setAttribute("src", randomSite());
//   showlocation.innerText = stumbleWindow.location.href;
  setInterval(countDown, 1000);
});

let x = 6;
function countDown() {
  x -= 1;
//   console.log(x);
  document.getElementById("countdowntarget").innerHTML = x;
  if (x === 0){
    stumbleWindow.setAttribute("src", randomSite());
    x = 6;

  } 
};