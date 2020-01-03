let button = document.getElementById("time");


let myTime = setInterval(myClock,1000);

function myClock(){
    let d = new Date();
    document.getElementById("showIt").innerHTML = d.toLocaleTimeString();
}


let stop = document.getElementById("stop")

stop.addEventListener('click', function(){
    document.getElementById("stop").style.visibility = "hidden";
    //create the div to set everything in
    let div = document.createElement("stopwatch");
    div.classList.add("inside");
    //create the header
    let header = document.createElement("h1");
    header.innerHTML = "This is the Stopwatch!"
    div.append(header);

    //create button to start timer
    let stopBtn = document.createElement("BUTTON");
    stopBtn.innerHTML = "Start!";
    div.append(stopBtn);

    let lapBtn = document.createElement("BUTTON");
    lapBtn.innerHTML = "Lap!";
    div.append(lapBtn);

    //create a p tage for the stopwatch to get appended too
    let watch = document.createElement("p");
    let lap = document.createElement("ol");

    stopBtn.addEventListener('click',function(){
        stopBtn.style.visibility = "hidden"
        let clock = new Date();
        clock.setHours(0,0,0,0);

        setInterval(function(){
            clock.setSeconds(clock.getSeconds()+1);
            watch.innerHTML = clock.toTimeString();
            div.append(watch);
        } ,1000);
    });

    //create a counter and add a eventlistner to the lapBtn.
    let counter = 0;
    lapBtn.addEventListener('click',function(){
        counter++;
        let lapTimes = document.getElementById("lapTimes");
        let list = document.createElement("ol");
        let move = document.createElement("li");
        
        list.innerText = `Lap:${counter} `;
        move = watch.innerHTML;
        list.append(move);
        lapTimes.append(list);
       
    })
   
    //append the div to the document
    let target = document.getElementById("target");
    target.insertBefore(div, target.firstChild);
});
let timer = document.getElementById("timer");
timer.style.display = "none";
let countDown = document.getElementById("countDown");
// let selector = document.getElementById("selector");
// selector.style.display = "none";

countDown.addEventListener('click', function(){
    countDown.style.visibility = "hidden";
    // selector.style.display = "block";
    timer.style.display = "block";
  
});
submit.addEventListener('click', function(event){
    event.preventDefault();

    let number = document.getElementById("number");
    let operator = document.getElementById("operator");
    let seconds = document.getElementById("seconds");
    let minutes = document.getElementById("minutes");
    // let select = document.getElementById("selector");
    let hours = document.getElementById("hours");

    let numberVal = number.value;
    let operatorVal = operator.value;
    let secondsVal = seconds.value;
    let minutesVal = minutes.value;
    let hoursVal = hours.value

    console.log(numberVal)
    
});

