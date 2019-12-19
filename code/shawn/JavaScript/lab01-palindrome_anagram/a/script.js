
function is_palindrome(input_str){
    let compare_str = ''
    for(let i=input_str.length-1; i>-1; i--){
        compare_str += input_str[i];
    }
    console.log(compare_str)
    return input_str === compare_str;
}

function are_anagrams(words){
    let prepped_words = [];
    let string_to_push = '';

    for (let word of words){
        string_to_push = word.toLowerCase();
        string_to_push = string_to_push.trim();
        string_to_push = string_to_push.replace(' ', '');
        string_to_push = string_to_push.split('');
        string_to_push = string_to_push.sort()
        string_to_push = string_to_push.join('')
        string_to_push = string_to_push.trim();

        prepped_words.push(string_to_push);
    }

    alert('prepped words ' + prepped_words);
    for (let i = 0; i < prepped_words.length; i++){
        if (prepped_words[i] !== prepped_words[0]){
            alert(`comparing ${prepped_words[i]} to ${prepped_words[0]}`)
            return false;
        }
    }

    return true;
}


let run_flag = true
while (run_flag){
    let command = prompt("Enter 'a' for anagram, 'p' for palindrome, or 'q' to quit: ")
    if (command === 'q'){
        alert("quitting")
        run_flag = false;
    } else if (command === 'p'){
        let p = prompt("Enter a work to check for palindromedness: ")
        if (is_palindrome(p)) alert(`${p} is a palindrome!`);
        else alert(`${p} is not a palindrome`)
    } else if (command === 'a') {
        let input_flag = true;
        let words = []
        while (input_flag) {
            let user_input = prompt("Enter words to check or 'done': ");
            if (user_input === 'done') input_flag = false;
            else words.push(user_input);
        }
        let check_anagrams = are_anagrams(words);
        if(check_anagrams) alert(`Those words ${words} are anagrams!`);
        else alert(`Those words ${words} are not anagrams.`)
    }   
}
