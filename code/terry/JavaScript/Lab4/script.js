loadEvents();
// load every event in the page
function loadEvents() {
    document.querySelector('form').addEventListener('submit', submit);
    document.getElementById('clear').addEventListener('click', clearList);
    document.querySelector('ul').addEventListener('click', deleteOrTick);
}

// subit data function
function submit(e) {
    e.preventDefault();
    let itemList;
    let input = document.querySelector('input');
    if (input.value != '')
        additem(input.value);
    input.value = '';
}

// add items
function additem(item) {
    let ul = document.querySelector('ul');
    let li = document.createElement('li');
    li.innerHTML = `<span class="delete">x</span><input type="checkbox"><label>${item}</label>`;
    ul.appendChild(li);
    document.querySelector('.itemsBoard').style.display = 'block';
}

// clear the LIST
function clearList(e) {
    let ul = document.querySelector('ul').innerHTML = '';
}

// deleteTick
function deleteOrTick(e) {
    if (e.target.className == 'delete')
        deleteitem(e);
    else {
        tickitem(e);
    }
}

// delete item
function deleteitem(e) {
    let remove = e.target.parentNode;
    let parentNode = remove.parentNode;
    parentNode.removeChild(remove);
}

// tick a item
function tickitem(e) {
    const item = e.target.nextSibling;
    if (e.target.checked) {
        item.style.textDecoration = "line-through";
        item.style.color = "blue";
    } else {
        item.style.textDecoration = "none";
        item.style.color = "black";
    }
}