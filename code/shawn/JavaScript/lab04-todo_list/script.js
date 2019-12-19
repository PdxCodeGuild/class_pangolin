// class for each todo item
class ToDo{
    constructor(inText){
        this.text = inText;
        this.dateCreated = new Date().toString();
        this.dateCompleted;
        this.isCompleted = false;
    }
}

// get items from DOM
let inputText = document.getElementById("input-text");
let buttonSubmit = document.getElementById("button-submit");
let buttonCompleteSelected = document.getElementById("button-complete-selection");
let buttonDeleteSelected = document.getElementById("button-delete-selection");
let targetActive = document.getElementById("target-active");
let targetCompleted = document.getElementById("target-completed");

// list for holding todo items
var toDoList = []

// event listener for submit button.  adds todo item to list
buttonSubmit.addEventListener("click", function(){
    // create new item
    let item = new ToDo(inputText.value);

    // add to list
    toDoList.push(item);

    // update items
    renderToDoList();
    
});

// PICK UP HERE   selection action buttons
buttonCompleteSelected.addEventListener('click', function(){
    let checkboxes = document.querySelectorAll("input[type='checkbox'].item-checkbox");
    for (let box of checkboxes){
        if(box.checked){
            // need to figure out how to lookup the item in ToDo list?  maybe create a hidden element for index?
            box.parentElement.remove();
        }
    }
});
buttonRemoveSelected.addEventListener('click', function(){
    let checkboxes = document.querySelectorAll("input[type='checkbox'].item-checkbox");
    for (let box of checkboxes){
        if(box.checked){

        }
    }
});


// function for rendering all ToDo items
function renderToDoList(){

    // remove existing items
    targetActive.innerHTML = '';
    targetCompleted.innerHTML = ''; 

    // iterate through all ToDo items
    // for (let item of toDoList){
    for(let i = 0; i < toDoList.length; i++){
        
        // create HTML elements
        let outerDiv = document.createElement('div');
        let innerDiv = document.createElement('div');
        let itemText = document.createElement('h3');
        let createdLabel = document.createElement('p');
        let completedLabel = document.createElement('p');
        let itemCreatedDate = document.createElement('p');
        let itemCompletedDate = document.createElement('p');
        let checkbox = document.createElement('input');
        let completeBut = document.createElement('button');
        let removeBut = document.createElement('button');

        // add classes
        outerDiv.classList.add("todo-item-outer");
        innerDiv.classList.add("todo-item-inner");
        itemText.classList.add("item-text");
        completedLabel.classList.add("date-label");
        createdLabel.classList.add("date-label");
        itemCreatedDate.classList.add("item-date");
        itemCompletedDate.classList.add("item-date");
        completeBut.classList.add("item-complete-button");
        removeBut.classList.add("item-remove-button");
        checkbox.classList.add("item-checkbox");
        
        // set values/attributes
        completeBut.innerText = "Complete";
        removeBut.innerText = "Remove";
        checkbox.type = "checkbox";
        itemText.innerText = toDoList[i].text;
        createdLabel.innerText = "created: "
        completedLabel.innerText = "completed: "
        itemCreatedDate.innerText = toDoList[i].dateCreated;
        itemCompletedDate.innerText = toDoList[i].dateCompleted;
        itemCompletedDate.hidden = true;
        completedLabel.hidden = true;

        // set target for item...active or completed
        let target;
        if(toDoList[i].isCompleted){
            target = targetCompleted;
            completeBut.hidden = true;
            toDoList[i].dateCompleted = new Date().toString();
            itemCompletedDate.innerText = toDoList[i].dateCompleted;
            itemCompletedDate.hidden = false;
            completedLabel.hidden = false;
        } else {
            target = targetActive;
        }

        // add to page
        outerDiv.append(completeBut);
        outerDiv.append(removeBut);
        outerDiv.append(checkbox);
        outerDiv.append(createdLabel);
        outerDiv.append(itemCreatedDate);
        outerDiv.append(completedLabel);
        outerDiv.append(itemCompletedDate);
        innerDiv.append(itemText);
        outerDiv.append(innerDiv);
        target.append(outerDiv)

        // event listeners for newly created buttons
        completeBut.addEventListener('click', function(){
            toDoList[i].isCompleted = true;
            renderToDoList();
        });
        removeBut.addEventListener('click', function(){
            toDoList.splice(i,1);
            renderToDoList();
        });

    }
};

