// Create a close button and append it to each list
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span);
}

// Click on a close button to hide current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        var div = this.parentElement;
        dif.style.display = "none";
    }
}

// Move checked items to bottom of list

let list1 = document.querySelector("ul");
list1.addEventListener('click', function(ev) {
    if (ev.target.tagName === "LI") {
        list1.removeChild(ev.target)
        list1.appendChild(ev.target)
    }
}, false);

// Add checked symbol and strikethrough on click
var list = document.querySelector("ul");
list.addEventListener('click', function(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked')
    }
}, false);

// Create new list item when clicking on Add button
function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === "") {
        alert("Please write something");
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

// Create new list item with Enter/Return key
// var input = document.getElementsByTagName("myInput");

// input.addEventListener("keyup", function(event) {
//     if (event.keyCode === 13) {
//         event.preventDefault();
//         document.getElementById("addBtn").click();
//     }
// });