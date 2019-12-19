let my_str = document.getElementById('my_str');
let new_str = document.getElementById('new_str');
let btn = document.getElementById('encrypt-btn');


function rot13(my_str) {
    var re = new RegExp("[a-z]", "i");
    var min = 'A'.charCodeAt(0);
    var max = 'Z'.charCodeAt(0);
    var factor = 13;
    var result = "";
    str = my_str;

    for (var i = 0; i < str.length; i++) {
        result += (re.test(str[i]) ?
            String.fromCharCode((str.charCodeAt(i) - min + factor) % (max - min + 1) + min) : str[i]);
    }

    return result;

}


btn.addEventListener('click', function() {
    new_str = rot13(my_str.value)
    console.log(new_str)
    document.getElementById("new_str").innerHTML = (`<h6>Your obfuscated word is:  ${new_str}</h6>`);
});