// to do app
// written by Rhornberger
// last updated december 26,2019

// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName('LI');
var i;
for (i = 0; i < myNodelist.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode('/u00D7');
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none"; 
    }
}
// move a clicked item in the list to the bottom of the list
let list1 = document.querySelector("ul");
list1.addEventListener('click', function(ev){
    if (ev.target.tagName === "LI"){
        list1.removeChild(ev.target)
        list1.appendChild(ev.target)
    }
}, false);

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector("ul");
list.addEventListener('click', function(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked')
    }
}, false);

//  create a new list item when clicking on the "Add" button
function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must add something to your todo list! No one has this much free time.");
    } else {
        document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value = "";

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }
}
