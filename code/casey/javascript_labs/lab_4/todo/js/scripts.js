const form = document.querySelector('form');
const ul = document.querySelector('ul');
const button = document.querySelector('button');
const input = document.getElementById('item');

let itemsArray = localStorage.getItem('items') ?
JSON.parse(localStorage.getItem('items')) : [];

localStorage.setItem('items', JSON.stringify(itemsArray));
const data = JSON.parse(localStorage.getItem('items'));

const liMaker = (text) => {
    var li = document.createElement('li');
    li.textContent = text;
    ul.appendChild(li);
    
    var clearBtn = document.createElement('button');
    clearBtn.innerHTML = "Clear Item";
    ul.appendChild(clearBtn);
    clearBtn.addEventListener('click', function() {
        localStorage.clear();
        while (ul.firstChild) {
            ul.removeChild(li);
            ul.removeChild(clearBtn);
            ul.removeChild(completedBtn);
        }
        itemsArray = [];
    });

    var completedBtn = document.createElement('button');
    completedBtn.innerHTML = "Completed";
    ul.appendChild(completedBtn);
    completedBtn.addEventListener('click', function() {
        localStorage.clear();
        while (ul.firstChild) {
            li.style.setProperty("text-decoration", "line-through");
            ul.removeChild(completedBtn);
        }
        itemsArray = [];
    });
};

form.addEventListener('submit', function(e) {
    e.preventDefault();

    itemsArray.push(input.value);
    localStorage.setItem('items', JSON.stringify(itemsArray));

    liMaker(input.value);
    input.value = "";
});

data.forEach(item => {
    liMaker(item);
});

button.addEventListener('click', function() {
    localStorage.clear();
    while (ul.firstChild) {
        ul.removeChild(ul.firstChild);
    }
    itemsArray = [];
});