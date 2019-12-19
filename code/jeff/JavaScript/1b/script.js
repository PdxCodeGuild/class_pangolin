var cards = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'ten': 10,
    'j': 10,
    'q': 10,
    'k': 10
}

let one = document.getElementById('one');
let two = document.getElementById('two');
let three = document.getElementById('three');
let a = document.getElementById('a');
let b = document.getElementById('b');
let c = document.getElementById('c');
let btn = document.getElementById('advise-btn');
let advice = document.getElementById('advice')

function card_eval(card1, card2, card3) {
    var tot = cards[card1] + cards[card2] + cards[card3]
    if (tot < 17) {
        advice = 'Based on your cards, my advice is: Hit.'
    } else if ((17 <= tot) && (tot < 21)) {
        advice = 'Based on your cards, my advice is: You should stay.'
    } else if (tot === 21) {
        advice = 'Blackjack. You win!'
    } else if (tot > 21) {
        advice = 'Bust. You lose!'
    }
    return advice
}

// card_eval(a, b, c);

btn.addEventListener('click', function() {
    calc = card_eval(one.value, two.value, three.value)
    console.log(calc)
    console.log(advice)
    AddAChild(calc)
});

function AddAChild(param) {
    var newElem = document.createElement("div");
    newElem.innerHTML = `<h6>${param}</h6>`;

    var container = document.getElementById("container");
    container.appendChild(newElem);
}

function lowVal(inElement) {
    return inElement.value.toLowerCase()
}

// function myFunction() {
//     document.getElementById("input").reset();
// }