let wordOne;
let wordTwo;
let word_one = document.getElementById("word_one");
let word_two = document.getElementById("word_two");
let submit = document.getElementById("submit");
let results = document.getElementById("results");

submit.addEventListener('click', function() {
    transformOne(word_one.value);
    transformTwo(word_two.value);
    // console.log(word_one.value);
    // console.log(wordOne);
    if (wordOne == wordTwo) {
        results.innerText = "Yes, these are anagrams.";
    } else {
        results.innerText = "No, these are not anagrams.";
    }
});

function transformOne(word_one) {
    word_one = word_one.replace(" ", "");
    wordOne = word_one.toLowerCase();
    wordOne = wordOne.split('');
    wordOne = wordOne.sort();
    wordOne = wordOne.toString();
    // console.log(wordOne);
    return wordOne;
}

function transformTwo(word_two) {
    word_two = word_two.replace(" ", "");
    wordTwo = word_two.toLowerCase();
    wordTwo = wordTwo.split('');
    wordTwo = wordTwo.sort();
    wordTwo = wordTwo.toString();

    return wordTwo;
}