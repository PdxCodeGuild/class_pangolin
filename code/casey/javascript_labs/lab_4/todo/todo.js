let item = document.getElementById("item");
let add = document.getElementById("add");
let list = document.getElementById("list");
let completed = document.getElementById("completed");

function addItem(e) {
    if (item.value) {
        let li = document.createElement("li");
        li.innerText = item.value;
        list.appendChild(li);
    }
};

add.addEventListener('click', addItem);
item.addEventListener('keydown', function (e) {
    if (e.keyCode === 13) {
        addItem(e);
    }
});



