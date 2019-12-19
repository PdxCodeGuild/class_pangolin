// class for each todo item
class ToDo{
    constructor(inText){
        this.text = inText;
        this.dateCreated = new Date().toString();
        this.dateCompleted;
        this.isCompleted = false;
        this.id = Math.random();    // id will be used for looking up items when doing selection actions
    }
}

// get items from DOM
let inputText = document.getElementById("input-text");
let buttonSubmit = document.getElementById("button-submit");
let buttonCompleteSelected = document.getElementById("button-complete-selection");
let buttonDeleteSelected = document.getElementById("button-delete-selection");
let targetActive = document.getElementById("target-active");
let targetCompleted = document.getElementById("target-completed");
let activeCount = document.getElementById("active-count");
let completedCount = document.getElementById("completed-count");

// list for holding todo items
var toDoList = []

// event listener for submit button (mouse).  adds todo item to list
buttonSubmit.addEventListener("click", function(){
    // create new item
    let item = new ToDo(inputText.value);

    // add to list
    toDoList.push(item);

    // clear text from input field
    inputText.value = '';

    // update items
    renderToDoList();
    
});
// event listener for submit button (enter).  adds todo item to list
inputText.addEventListener("keydown", function(event){
    if(event.key === 'Enter'){
        // create new item
        let item = new ToDo(inputText.value);

        // add to list
        toDoList.push(item);
        
        // clear text from input field
        inputText.value = '';

        // update items
        renderToDoList();
    }
});

// event listener for group completions
buttonCompleteSelected.addEventListener('click', function(){
    let checkboxes = document.querySelectorAll("input[type='checkbox'].item-checkbox");
    for (let box of checkboxes){
        if(box.checked){
            // get index of item to be marked completed
            let id = box.getAttribute("itemId");
            let x;
            for (let i = 0; i < toDoList.length; i++){
                if(id === toDoList[i].id.toString()){
                    x = i;
                }
            }
            // complete item at index x
            toDoList[x].isCompleted = true;
            // render items
            renderToDoList();
        }
    }
});
// event listener for group deletions
buttonDeleteSelected.addEventListener('click', function(){
    let checkboxes = document.querySelectorAll("input[type='checkbox'].item-checkbox");
    for (let box of checkboxes){
        if(box.checked){
            // get index of item to be marked completed
            let id = box.getAttribute("itemId");
            let x;
            for (let i = 0; i < toDoList.length; i++){
                if(id === toDoList[i].id.toString()){
                    x = i;
                }
            }
            // remove item at index x
            toDoList.splice(x,1);
            // render items
            renderToDoList();
        }
    }
});

// function for rendering all ToDo items
function renderToDoList(){

    // remove existing items
    targetActive.innerHTML = '';
    targetCompleted.innerHTML = ''; 

    // iterate through all ToDo items
    let activeCounter = 0;
    let completedCounter = 0;

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
        checkbox.setAttribute("itemId", toDoList[i].id.toString());
        itemText.innerText = toDoList[i].text;
        createdLabel.innerText = "created: "
        completedLabel.innerText = "completed: "
        itemCreatedDate.innerText = toDoList[i].dateCreated;
        itemCompletedDate.innerText = toDoList[i].dateCompleted;

        // by default, rendered as active items.  do these additional actions if completed
        let target;
        if(toDoList[i].isCompleted){
            target = targetCompleted;
            completeBut.hidden = true;
            toDoList[i].dateCompleted = new Date().toString();
            itemCompletedDate.innerText = toDoList[i].dateCompleted;
            outerDiv.classList.add("completed")
            completedCounter++;
        } else {
            outerDiv.classList.add("active")
            target = targetActive;
            activeCounter++;
        }

        // add to page
        innerDiv.append(completeBut);
        innerDiv.append(removeBut);
        innerDiv.append(checkbox);
        innerDiv.append(createdLabel);
        innerDiv.append(itemCreatedDate);
        if(toDoList[i].isCompleted) {
            innerDiv.append(completedLabel);
            innerDiv.append(itemCompletedDate);
        }
        outerDiv.append(innerDiv);
        outerDiv.append(itemText);
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
     
    // update counts
    activeCount.innerText = activeCounter;
    completedCount.innerText = completedCounter;
};

