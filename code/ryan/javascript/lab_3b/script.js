let first = document.getElementById('first_word');
let second = document.getElementById('second_word');
let button = document.getElementById('button');
let answer = document.getElementById('answer');

function anagram() {
    let wordAna1 = first.value.toLowerCase().replace(/ /g, "").split("").sort().join("");
    let wordAna2 = second.value.toLowerCase().replace(/ /g, "").split("").sort().join("");
    let wordPalin1 = first.value.toLowerCase().replace(/ /g, "").split("").join("");
    let wordPalin2 = first.value.toLowerCase().replace(/ /g, "").split("").reverse().join("");
    
    if (wordAna1 === wordAna2) {
        result = "anagrams!";
    } else if (wordPalin1 === wordPalin2) {
        result = "This word is a palindrome!";
    } else {
        result = "neither an anagram or palindrome!";
    }
    if (result === "This word is a palindrome!") {
    answer.innerText = result;
    } else {
        answer.innerText = "These words are " + result;
    }
}

button.addEventListener('click', anagram);
