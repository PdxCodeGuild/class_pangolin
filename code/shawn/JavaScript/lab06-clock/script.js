// get DOM elements
let dateOutputNums = document.getElementById("p-date-nums");
let dateOutputShort = document.getElementById("p-date-short");
let dateOutputLong = document.getElementById("p-date-long");
let timeOutput24 = document.getElementById("p-time-24");
let timeOutput12 = document.getElementById("p-time-12");

// set some variables to be referenced outside of tick function
let nowDay;                     // DD 1-31
let nowDayString;               // 'Monday' 'Tuesday' etc
let nowTime24;                  // HH:MM:SS
let nowTime12;                  // HH:MM:SS am/pm
let hours12;                    // array for non-military time [hr, am/pm]
let nowMonthString;             // 'Janurary' 'February' etc
let nowMonth;                   // Month as number 0-11
let nowYear;                    // Year number
let nowDateStringObjectShort;   // Data object formatted:  'Thu Apr 12 2018'
let nowDateStringObjectLong;    // Data object formatted:  'April 12, 2018'
let nowDateStringHomebrew;      // Homebrew format: MM/DD/YYYY


// tick function, ran every second
function tick(){
    // new Date object
    let now = new Date();

    // get date (Date object methods)
    nowDay = now.getDate();
    nowMonth = now.getMonth();
    nowYear = now.getFullYear();
    let nowDayOfWeek = now.getDay();
    nowTime24 = now.toTimeString().split(" ")[0];     // military time

    // homebrew
    // day string
    if (nowDayOfWeek===0) nowDayString = "Sunday";
    else if (nowDayOfWeek===1) nowDayString = "Monday";
    else if (nowDayOfWeek===2) nowDayString = "Tuesday";
    else if (nowDayOfWeek===3) nowDayString = "Wednesday";
    else if (nowDayOfWeek===4) nowDayString = "Thursday";
    else if (nowDayOfWeek===5) nowDayString = "Friday";
    else if (nowDayOfWeek===6) nowDayString = "Saturday"; 
    // month string
    if (nowMonth===0) nowMonthString = "January";
    else if (nowMonth===1) nowMonthString = "February";
    else if (nowMonth===2) nowMonthString = "March";
    else if (nowMonth===3) nowMonthString = "April";
    else if (nowMonth===4) nowMonthString = "May";
    else if (nowMonth===5) nowMonthString = "June";
    else if (nowMonth===6) nowMonthString = "July"; 
    else if (nowMonth===7) nowMonthString = "August"; 
    else if (nowMonth===8) nowMonthString = "September"; 
    else if (nowMonth===9) nowMonthString = "October"; 
    else if (nowMonth===10) nowMonthString = "November"; 
    else if (nowMonth===11) nowMonthString = "December"; 
    // twelve hour time
    let hours24 = nowTime24.split(":")[0]
    if (hours24==0) hours12 = [12,'am'];
    else if (hours24==1) hours12 = [1,'am'];
    else if (hours24==2) hours12 = [2,'am'];
    else if (hours24==3) hours12 = [3,'am'];
    else if (hours24==4) hours12 = [4,'am'];
    else if (hours24==5) hours12 = [5,'am'];
    else if (hours24==6) hours12 = [6,'am'];
    else if (hours24==7) hours12 = [7,'am'];
    else if (hours24==8) hours12 = [8,'am'];
    else if (hours24==9) hours12 = [9,'am'];
    else if (hours24==10) hours12 = [10,'am'];
    else if (hours24==11) hours12 = [11,'am'];
    else if (hours24==12) hours12 = [12,'pm'];
    else if (hours24==13) hours12 = [1,'pm'];
    else if (hours24==14) hours12 = [2,'pm'];
    else if (hours24==15) hours12 = [3,'pm'];
    else if (hours24==16) hours12 = [4,'pm'];
    else if (hours24==17) hours12 = [5,'pm'];
    else if (hours24==18) hours12 = [6,'pm'];
    else if (hours24==19) hours12 = [7,'pm'];
    else if (hours24==20) hours12 = [8,'pm'];
    else if (hours24==21) hours12 = [9,'pm'];
    else if (hours24==22) hours12 = [10,'pm'];
    else if (hours24==23) hours12 = [11,'pm'];
    nowTime12 = `${hours12[0]}:${nowTime24.split(":")[1]}:${nowTime24.split(":")[2]} ${hours12[1]}`

    // date formats
    nowDateStringObjectShort = now.toDateString();
    nowDateStringObjectLong  = `${nowMonthString} ${nowDay}, ${nowYear}`
    nowDateStringHomebrew = `${nowMonth+1}/${nowDay}/${nowYear}`
    
    // update clock
    updateClock();
}

// start clock, tick every 1000ms/1sec
window.setInterval(tick, 1000);

// function for updating clock
function updateClock(){
    dateOutputNums.innerText = nowDateStringHomebrew;
    dateOutputShort.innerText = nowDateStringObjectShort;
    dateOutputLong.innerText = nowDateStringObjectLong;
    timeOutput24.innerText = nowTime24;
    timeOutput12.innerText = nowTime12;

}