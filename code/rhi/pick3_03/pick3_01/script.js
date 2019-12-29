// average numbers 
//  part one of the pick three javascript lab
//  written by Rhornberger
// last updated dec 16,2019

let user_choice = prompt('Please enter a number or enter done when you are finished').toLowerCase();

let user_list = []
while (user_choice !== 'done'){
    user_list.push(user_choice);
    user_choice = prompt('Please enter a number or enter done when you are finished').toLowerCase();
}

alert(user_list)
alert(`${user_list.length} is the number of numbers in your array`)

user_list = user_list.map(function(num) {
    return parseInt(num);
});

let tot = 0
user_list = user_list.map(function(num) {
    tot = tot + num;
    return tot
});
alert(`${tot} is the total of the numbers you entered`)

tot = tot / user_list.length
tot = Math.floor(tot)
alert(`${tot} is the average of the numbers you entered!`)
alert('Thank you come again.')