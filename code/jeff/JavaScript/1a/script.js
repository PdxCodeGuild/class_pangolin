var cards = ['a', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6, '7', 7, '8', 8, '9', 9, '1', 10, 'ten', 10, 'j', 10, 'q', 10, 'k', 10]

function card_eval(card1, card2, card3) {
    var tot = cards[card1] + cards[card2] + cards[card3]
    if (tot < 17) {
        alert('Hit.')
    } else if (tot in range(17, 21)) {
        alert('You should stay.')
    } else if (tot == 21) {
        alert('Blackjack. You win!')
    } else if (tot > 21) {
        alert('Bust. You lose!')
    }

}

var one = prompt('Enter your 1st card(A, 2-10, J, Q, K): ').toLowerCase();
var a = one[0]
var two = prompt('Enter your 2nd card(A, 2-10, J, Q, K): ').toLowerCase();
var b = two[0]
var three = prompt('Enter your 3rd card(A, 2-10, J, Q, K): ').toLowerCase();
var c = three[0]
card_eval(a, b, c);