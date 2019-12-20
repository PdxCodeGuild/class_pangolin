// credit card validator
//  part one of the pick three javascript lab
//  written by Rhornberger
// last updated dec 16,2019
let u_num = document.getElementById("num");
let answer = document.getElementById("validate");
let result = document.getElementById("result");



function is_valid() {
    // turning my string of numbers into a list of intergers 
    output = [],
    u_num = u_num.value.toString();

    for (var i = 0, len = u_num.length; i < len; i += 1) {
        output.push(u_num.charAt(i));
    }

    // u_num = u_num.split(' ')
    // u_num = u_num.map(Number);
    console.log(output)

    // slice the last number off my list
    let u_num2 = output.pop();
    // u_num2 = u_num2.map(Number)
    console.log(u_num2)

    // turn the rest of the array around, the ending number is now the first number
    let cc_num = output.slice(0,15);
    cc_num1 = cc_num.reverse();
    console.log(cc_num1)


    // double every other item in the list
    // let res1 = []
    let res = cc_num1.map(function(val, i) {
        if(i % 2 === 0) {
            return val * 2
        } else {
            return val
        }
    });
    console.log(res)

    // subtract 9 from all number greater than 9
    let res2 = res.map(function(val) {
        if (val > 9) {
            return val - 9
        } else {
            return val
        }
    });
    console.log(res2)

    // sum of all the values in the array
    let tot = 0
    res2 = res2.map(Number);
    res2.map(function(num) {
        tot = tot + num;
        // return tot
    });
    console.log(tot);

    // get the second digit of the returned tot number
    let tot2 = Math.floor(tot % 10);
    console.log(tot2);
    // compare the number from tot2 to the final number that was popped off in the beggining.
    if (tot2 === parseInt(u_num2)) {
        let para = document.createElement("P");
        para.innerText = 'Congradulations! This is a valid credit card number.';
        result.appendChild(para);
    } else {
        let para = document.createElement("P");
        para.innerText = `I am sorry ${u_num} is not a valid credit card number.`;
        result.appendChild(para);
    };
}
answer.addEventListener("click", is_valid)