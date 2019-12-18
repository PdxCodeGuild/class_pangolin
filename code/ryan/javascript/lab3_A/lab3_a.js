alert('Check for anagrams!!');
function check_anagram() {
    let first_word = prompt("What is your first word?");
    let second_word = prompt("What is your second word?");
    let f = first_word.split('').sort().join('');
    let s = second_word.split('').sort().join('');
    if (f === s) {
        return true;
    } else {
        return false;
    }    
};

if (check_anagram() === true) {
    alert('These words are anagrams');
} else {
    alert('Not anagrams');
}

alert("Check for palindromes!!");
function check_palindrome() {
    let word = prompt("Enter word to check for palindrome:")
    if (word.split('').reverse().join('') === word) {
        return true;
    } else {
        return false;
    }
};

if (check_palindrome() === true) {
    alert("This word is a palindrome!!!")
} else {
    alert("Not a palindrome!!!")
}