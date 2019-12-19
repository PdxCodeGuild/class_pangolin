// credit card validator
//  part one of the pick three javascript lab
//  written by Rhornberger
// last updated dec 16,2019

// turning my string of numbers into a list of intergers 
let u_num = prompt('Please enter a credit card number: ').split(' ').map(Number);
// alert(u_num);

// slice the last number off my list
let u_num2 = u_num.pop();
// alert(u_num2)

// turn the rest of the array around, the ending number is now the first number
let cc_num = u_num.slice(0,15);
cc_num1 = cc_num.reverse();
// alert(cc_num1)

// double every other item in the list
// let res1 = []
let res = cc_num1.map(function(val, i) {
    if(i % 2 === 0) {
        return val * 2
    } else {
        return val
    }
});
// alert(res)

// subtract 9 from all number greater than 9
let res2 = res.map(function(val) {
    if (val > 9) {
        return val - 9
    } else {
        return val
    }
});
// alert(res2)

// sum of all the values in the array
let tot = 0
let user_list = res2.map(function(num) {
    tot = tot + num;
    return tot
});
// alert(tot)

// get the second digit of the returned tot number
let tot2 = Math.floor(tot % 10);
// alert(tot2)

// compare the number from tot2 to the final number that was popped off in the beggining.
if (tot2 === u_num2) {
    alert('Congradulations! This is a valid credit card number.')
} else {
    alert(`I am sorry ${u_num} is not a valid credit card number.`)
}