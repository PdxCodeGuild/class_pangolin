function rotateThirteen(plainText, shift) {
    let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    let cipherInput = plainText.split('');
    let cipherOutput = [];
    for (letter of cipherInput) {
        let x = letters.indexOf(letter);
        let y;
        x += shift;
        if (x >= 26) {
            x -= 26
        }
        y = letters[x];
        cipherOutput.push(y) 
    }
    alert(cipherOutput.join(''));
    return cipherOutput.join('')
    };

let shift = parseInt(prompt("Enter the number of steps you would like to shift (1-13). "));  
let text = prompt("Enter the text you would like to encrypt. ").toLowerCase();
alert(rotateThirteen(text, shift));