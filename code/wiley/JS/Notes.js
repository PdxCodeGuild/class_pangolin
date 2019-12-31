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

// MAP REDUCE AND FILTER //
// map is similar to list comprehension,  does something to an array, and returns a new value //

let myArray = [1,2,3,4,5,6,5,4,3,2,1]

let squaredArray = myArray.map(function(x) {
    return x**2;
});
// This is basically a list comprehension of (in python) squared_list=[x**2 for x in old_list] //
// in map() you can apply an iteration number (i=), this is not possible with list comprehension
// In the function you can now 
let squaredArray = myArray.map(function(x, i) {
    if (i % 2 == 0) {
        return x*2;
    }
    else {
        return x;
    };
});

// this above map function only doubles x if its index is even.

//the const declaration demands a variables and information with it.  It is (mostly) immutable.  Dictionaries can be updates, but strings are immutable.  Same scope as let
const me = "wiley";

// canvas in HTML.  getContext('2d'), for a 2d canvas
// cheat sheet for canvas is in the calss github and more stuff in mdn and w3school
// to center text you need to put the x at (x - (ctx.measureText('text').width / 2), y)
// this works by measuring the width of the text you are entering and subtracts half of that from the x point you entered.  This should be cetnered if done correctly. 
// you have to et canvas width and height in HTML, not css
