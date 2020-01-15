setInterval(updateClock, 1000)
function updateClock() {
  let target = document.getElementById("clock");
  var currentTime = new Date();
  var currentHours = currentTime.getHours();
  var currentMinutes = currentTime.getMinutes();
  var currentSeconds = currentTime.getSeconds();

  currentMinutes = (currentMinutes < 10 ? "0" : "") + currentMinutes;
  currentSeconds = (currentSeconds < 10 ? "0" : "") + currentSeconds;

  var timeOfDay = currentHours < 12 ? "AM" : "PM";
  currentHours = currentHours > 12 ? currentHours - 12 : currentHours;
  currentHours = currentHours == 0 ? 12 : currentHours;

  var currentTimeString =
    currentHours +
    ":" +
    currentMinutes +
    ":" +
    currentSeconds +
    " " +
    timeOfDay;
  target.innerHTML = currentTimeString;
  console.log(currentTimeString);
//   return currentTimeString;
}

// var clock = setInterval(myTimer, 1000);

// function myTimer() {
//   var currentTime = new Date();
//   document.getElementById("clock").innerHTML = currentTime.toLocaleTimeString();
// }
