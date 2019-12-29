function is_palindrome(input_str) {
    input_str = input_str.toLowerCase()
    input_str = input_str.replace(/ /g, '')
    let compare_str = ''
    for (let i = input_str.length - 1; i > -1; i--) {
        compare_str += input_str[i];
    }
    return input_str === compare_str;
}

function are_anagrams(words) {
    let prepped_words = [];
    let string_to_push = '';

    for (let word of words) {
        string_to_push = word.toLowerCase();
        string_to_push = string_to_push.split('');
        string_to_push = string_to_push.sort()
        string_to_push = string_to_push.join('')

        prepped_words.push(string_to_push);
    }


        for (let i = 0; i < prepped_words.length; i++) {
            if (prepped_words[i] !== prepped_words[0]) {
                return false;
            }
        }
    if (prepped_words.length > 0) {
        return true;
    }
}

let palindromeArea = document.getElementById("palindrome-area")
let anagramArea = document.getElementById("anagram-area")
let palindromeResult = document.getElementById("palindrome-result")
let anagramResult = document.getElementById("anagram-result")

palindromeArea.addEventListener('input', function () {
    if (is_palindrome(palindromeArea.value)) {
        palindromeResult.innerText = "Yes, this is a palindrome.";
        palindromeResult.style.color = 'green';
    }

    else if (!is_palindrome(palindromeArea.value)) {
        palindromeResult.innerText = "No, not a palindrome.";
        palindromeResult.style.color = 'red';
    }


});
anagramArea.addEventListener('input', function () {
    let words = anagramArea.value.trim().split(/\s+/g);

    if (are_anagrams(words)) {
        anagramResult.innerText = "Yes, these are anagrams.";
        anagramResult.style.color = 'green';
    }
    else {
        anagramResult.innerText = "No, not anagrams.";
        anagramResult.style.color = 'red';
    }
});
