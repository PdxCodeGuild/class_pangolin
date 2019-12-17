// function rot13(my_str) {
//     eng = 'abcdefghijklmnopqurstuvwxyz'
//     crypt = ''
//     for (char in my_str)
//         crypt += eng((eng.find(char) + 13) % 26)
//     alert(crypt);
// }
// var my_str = prompt('What word would you like to obfuscate today? ');
// var new_str = rot13(my_str)
// console.log(new_str)
// prompt(`Your obfuscated word is:  ${new_str}`)
function rot13(my_str) {
    var re = new RegExp("[a-z]", "i");
    var min = 'A'.charCodeAt(0);
    var max = 'Z'.charCodeAt(0);
    var factor = 13;
    var result = "";
    str = my_str.toUpperCase();

    for (var i = 0; i < str.length; i++) {
        result += (re.test(str[i]) ?
            String.fromCharCode((str.charCodeAt(i) - min + factor) % (max - min + 1) + min) : str[i]);
    }

    return result;
}
var my_str = prompt('What word would you like to obfuscate today? ');
var new_str = rot13(my_str)
console.log(new_str)
prompt(`Your obfuscated word is:  ${new_str}`)