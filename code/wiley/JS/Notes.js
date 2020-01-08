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




/* ------------APIs and AJAX------------------
AJAX stands for  Asynchronys Javascripts And XML 
API stands for application programming interface
An API is a standardizd way to get and receive data from a web service via HTTP requests (GET, POST, PUT, DELETE).
The API URL can contain GET parameters (query parameters).
API are just text.  Objects and arrays.  No method or functions will be used in it.  Javascript can read and parse the text and make it readable. 

AJAX request, old way: */

let quoteButton = document.getElementById("quoteButton");
let target = document.getElementById("target");

//create a new XMLHttpRequest
let req = new XMLHttpRequest();

//Define Event Listeners
req.addEventListener("progress", function(e){
    console.log(e.loaded);
});
req.addEventListener("error",function(e){
    console.log(e.status);
});
req.addEventListener("load", function(e){
    console.log(req.responseText);
});

//Open the request
//define the method of our request (POST,GET,PUT,DELETE), and the URL to send our request to.
req.open("GET", "https://favqs.com/api/qotd");

//above, you might want to use a template string in the URL so that you can dynaically generate your URL request.  ex:
`https://www.wiley.com/${document.getElementById("page-number").value}`;

//Set any request headers
//request headers can incluse encoded information.  This is more secure, and can include authentication keys from the user.  
req.setRequestHeader("Authorization", 'TOEKN token="token-key-here"');

//Send the request
//order matters Make sure your request is in the following oder or you won't get the results you expect:
//1) create a new respone
//2) Add event listeners
//3)Open the request
//4)Set headers
//5)Send the Request
req.send();


//Now we need to handle the response.  
//Our callback functions will work with our new data, instead of just console.log
req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    target.innerText = "Loading...";
});
req.addEventListener("error", function(e) {
    console.log(e.status);
    target.innerText = "Cannot load quote. Try again later!";
});
req.addEventListener("load", function(e){
    console.log(req.responseText);
    let resone = JSON.parse(req.responseText);
    console.log(this.response);
    let resultHTML =`
    <p>${response.quote.body}</p>
    <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>`
    target.innerHtml = resultHTML;
});

// Use an event listener to fire the request
let quoteButton = document.getElementById("quoteButton");
let target = document.getElementById("target");
let req = new XMLHttpRequest();

quoteButton.addEventListener("click", function(e){ //this button now fires the whole request below
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        console.log(response);
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        textTarget.innerHTML = resultHTML;
    });
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", 'Token token="YOUR_TOKEN_GOES_HERE"');
    req.send()
});


//Fetch and Axios are modern methods of to send HTTP requests and their responses
//uses "Promises", not fetch.  Meaning, there isn't anything here, but there will be soon. 
fetch('www.api.website.org/?format=json')
    .then(function(response){
    return response.joson();
    })
    .then(function(myJson) {
        console.log(myJson);
    })
    .catch(error => console.error(error));

//AXIOS: Axios is a third party javascript library.  You need to load this into your HTML, BEFORE your custom javascript files.  This is so that is loads into YOUR Javascript as well, otherwise you will get an undefined error.
//EXAMPLE:
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

//then in YOUR script
axios.get(url)
.then(function(response){
    console.log(response.data)
});

//Real use example:

let quoteButton = document.getElementById("quoteButton");

quoteButton.addEventListener('click', function(e) {
    axios({ //start the axios with a dictionary of the information you need to request.  the URL, Method, Headers, Params, Data etc. 
        url:"https://favqs.com/api/qotd",
        method: "GET",
        headers: {
            Authorization: 'Token token="98asha9s8dnk3j8skjans9"'
        }
    }).then(function(payload){
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        target.innerHTML = resultHTML;
    }).catch(function(error){})
});

//IMPERATIVE: code operating from top to bottom. 
