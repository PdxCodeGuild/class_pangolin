// average numbers 
//  part one of the pick three javascript lab
//  written by Rhornberger
// last updated dec 16,2019
let user_choice = document.getElementById("num");
let add_num = document.getElementById("add_num");
let done_btn = document.getElementById("done_btn");
let average = document.getElementById("tot")


let user_list = [];
console.log(user_list)
function makelist() {
    user_list.push(user_choice.value);
    console.log(user_list)
    let li = document.createElement("li");
    li.innerText = user_choice.value;
    results.appendChild(li);
};

function findaverage(){
    console.log('FINDING AVERAGE')
    user_list = user_list.map(function(num) {
        return parseInt(num);
    });
    let tot = 0
    user_list = user_list.map(function(num) {
        tot = tot + num;
        return tot;
    });
    console.log(tot);
    console.log(user_list.length);
    tot = tot / user_list.length;
    // tot = Math.floor(tot);
    
    let para = document.createElement("P");
    para.innerText = tot;
    average.appendChild(para);
};

add_num.addEventListener('click', makelist);
done_btn.addEventListener('click', findaverage);