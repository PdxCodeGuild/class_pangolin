var ones = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]
var twos = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

var tens = [
    '',
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

function textnum(num) {
    if (num === 0) {
        return 'zero';
    } else if (num > 0 && num <= 9) {
        return ones[num];
    } else if (num >= 10 && num <= 19) {
        return twos[num];
    } else if (num >= 20 && num <= 99) {
        var n1 = Math.floor(num / 10)
        var n2 = (num % 10)
        return tens[n1] + '-' + ones[n2]
    } else {
        alert("Number out of range")
    }
}
var x = prompt('Enter a number 0-99; ')
var num = parseInt(x);
alert(textnum(num))