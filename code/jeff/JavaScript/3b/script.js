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



function textnum() {
    console.log("hello from textnum")
    let num_element = document.getElementById('num');
    let num = num_element.value
    console.log(num)
    if (num === 0) {
        return 'zero';
    } else if ((num > 0) && (num <= 9)) {
        return ones[num];
    } else if ((num >= 10) && (num <= 19)) {
        return twos[num];
    } else if ((num >= 20) && (num <= 99)) {
        var n1 = Math.floor(num / 10)
        var n2 = (num % 10)
        return tens[n1] + '-' + ones[n2]
    } else {
        alert("Number out of range")
    }
}

let btn = document.getElementById("convert-btn");

btn.addEventListener('click', function() {
    calc = textnum(num)
    AddAChild(calc)
});

function AddAChild(param) {
    var newElem = document.createElement("div");
    newElem.innerHTML = `<h6>${param}</h6>`;

    var container = document.getElementById("container");
    container.appendChild(newElem);
}