// numbers to letters numbers 
//  part one of the pick three javascript lab
//  written by Rhornberger
// last updated dec 16,2019

// build the dictionaries

let ones_dict = {
    0: '', 
    1: 'one', 
    2: 'two', 
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six', 
    7: 'seven', 
    8: 'eight', 
    9: 'nine',
};

let ten_dict = {
    10: 'ten', 
    11: 'eleven', 
    12: 'twelve', 
    13: 'thirteen', 
    14: 'fourteen', 
    15: 'fifteen', 
    16: 'sixteen', 
    17: 'seventeen', 
    18: 'eighteen', 
    19: 'nineteen',
};

let tens_dict = {
    0: '', 
    1: '', 
    2: 'twenty', 
    3: 'thirty', 
    4: 'fourty', 
    5: 'fifty', 
    6: 'sixty', 
    7: 'seventy', 
    8: 'eighty', 
    9: 'ninety',
};

let hundreds_dict = {
    0: '', 
    1: 'one hundred', 
    2: 'two hundred', 
    3: 'three hundred', 
    4: 'four hundred', 
    5: 'five hundred', 
    6: 'six hundred', 
    7: 'seven hundred', 
    8: 'eight hundred', 
    9: 'nine hundred',
};

// build the function


function translate(user_num) {
    if (user_num === '0') {
        alert('Zero');
    }
    else if (user_num > 0 && user_num <= 9) {
        return ones_dict[user_num];
    }
    else if(user_num >= 10 && user_num <= 19) {
        return ten_dict[user_num];
    }
    else if(user_num >= 20 && user_num <= 99) {
        let n1 = Math.floor(user_num / 10);
        let n2 = (user_num % 10);
        return tens_dict[n1] + '-' + ones_dict[n2];
    }
    else if (user_num >= 100 && user_num <= 999) {
        let n0 = Math.floor(user_num / 100);
        let n1 = user_num.toString();
        n1 = n1[1]
        n1 = parseInt(n1)
        let n2 = (user_num % 10);
        return hundreds_dict[n0] + ' ' + 'and' + ' ' + tens_dict[n1] + '-' + ones_dict[n2];
    }
    else {
        return ('This number is outside of my computing powers!')
    }
    
}

let user_num = prompt('What number would you like converted?: ');
user_num = parseInt(user_num)
alert(translate(user_num));