/* Java Scipt Notes and practice


*/
let x = parseInt('4');
let y = parseFloat('4.20');
let z = x.toString();

let name = promt("Enter your name");
alert("Hello" + name + "! How are you?");
/* You can use input elements in HTML with a script 
ex: 
<input id="name_input" type="text">
<script>
    let bane_input = document.querySelector('#name_input');
    let name_value = name_input.value;
    alert(name_value);
</script>
*/

//console.log is nice to print variables and results to the console in order to debug things //


/* conditionals 
requires parentheses and curly-braces
*/

let temperature = 56;
if (temperature < 60) {
    alert('cold');
} else if (temperature < 80 ) {
    alert('warm');
} else {
    alert('hot');
}

//truthy and falsey. All values are truthy except for false, null, "", 0, undefined and NaN (not a number) //

let x = 0;
if (x) {
    console.log('true!');
} else {
    console.log('false!') ;
}

//ternary operator lets you perform an if else in one line. //
function min(a,b) {
    return (a < b)? a:b;
}

//array methods//
Array.length
Array.push(element)
Array.pop()
Array.splice()
Array.sort()
// etc, there are many options //


// FUNCTIONS //
//two ways to declair //
function add(a,b) {
    return a+b;
}

// or //

let add = function(a,b) {
    return a + b;
}

//the first one is a hoisted function, and the second on is undefined until it runs.  //


//day 2 JS notes//
/* DOM Manipulation.  Document Object Model 
You can select elements by class, type, name, tag and more.  
Basic example: document.getElementByID("id-name-here")

document.querySelector() returns the first found match
document.querySelectorAll() returns an array like object of all matches

Once you have a document object you can change its attributes 
ex: d.setAttriute("name", "so-bad")
*/
