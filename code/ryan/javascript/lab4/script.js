let todo = document.getElementById('item');
let button = document.getElementById('button');
let list = document.getElementById('list');
let complete = document.getElementById('complete');

button.addEventListener('click', function(){
    let li = document.createElement('li');
    li.innerText = todo.value;
    list.appendChild(li);
    todo.value = '';

    let deleteButton = document.createElement('button');
    deleteButton.innerText = 'Delete';
    li.appendChild(deleteButton);

    let completeButton = document.createElement('button');
    completeButton.innerText = 'Complete';
    li.appendChild(completeButton);

    deleteButton.addEventListener('click', function(){
        this.parentElement.remove();
    });

    completeButton.addEventListener('click', function(){
        completeMove = this.parentElement;
        complete.appendChild(completeMove);
        completeMove.style.textDecoration = 'line-through';
        this.remove();
    })
})






