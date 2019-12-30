/* Welcome to todolist.js: a simple program to manage your day to day to do's!
In this program you can: Add a thing you need to do, complete said thing, remove all completed events.
Maybe I can add a timestamp for when you add an item, and another for when you need to complete it.  

*/
let toDoArray = []
let newItem;
let timeAdded;
let webList;
let bottom;
let doneList;
function addItem() {
    // Button event function that adds an item to this items list and creates more buttons //
    newItem = document.getElementById("newitem");
    newItemTimeTargetRaw = document.getElementById("item-time");
    doneList = document.getElementById("doneList");

    //adding a target time and an added time to the freshToDo and then pushes each to do dictionary to the  master array //
    newItemTimeTarget = new Date(newItemTimeTargetRaw.value).toLocaleString();
    timeAdded = new Date().toLocaleString();
    freshToDo = ({"ToDoEvent": newItem.value,"TargetCompletionTime": newItemTimeTarget, "DateAdded": timeAdded});
    toDoArray.push(freshToDo);

    //adding the item to the HTML <ul> as a <li> and adding a checkbox for task completion with a default value of <li class="notDone"> 
    let toDoItem = document.createElement("li");
    toDoItem.innerText = `${freshToDo.ToDoEvent} by: ${freshToDo.TargetCompletionTime}. Added on: ${freshToDo.DateAdded}.`;
    toDoItem.classList.add("notDone");
    let finishedBtn = document.createElement("input");
    finishedBtn.type = "checkbox";
    finishedBtn.name = "completed";

    //event listener for the checkbox that toggles the <li> class as "done" or "notDone"
    webList = document.getElementById("list");
    webList.appendChild(toDoItem).appendChild(finishedBtn);
    finishedBtn.addEventListener("click", function() {

        console.log(finishedBtn.checked);
        if (finishedBtn.checked === true) {
            this.parentElement.classList.remove("notDone");
            this.parentElement.classList.add("done");
            console.log(this.parentElement);
            let doneToBeMoved = document.getElementsByClassName("done");
            doneList.appendChild(this.parentElement);
            console.log(doneList, this + "TEST");
            
        }
        else {
            this.parentElement.classList.remove("done");
            this.parentElement.classList.add("notDone");
            console.log(this.parentElement);
            webList.appendChild(this.parentElement);
        }
        if (Array.from(doneList.children)) {
            let dumb = document.getElementById("deleteBtn");
            console.log(dumb);
            dumb.style.display = "block";
        };
    });
   
    //clear the origin input fields' value for clean UI and easy new item adding
    newItem.value = null;
    newItemTimeTargetRaw.value = null;

    //creating a delete completed button at the bottom of the page
    let deleteBtn = document.createElement("button")
    deleteBtn.innerText = "delete completed tasks";
    deleteBtn.classList.add("deleteBtn");
    deleteBtn.id = "deleteBtn";
    bottom = document.getElementById("bottom");

    //preventing multiplying buttons for each added item. 
    let dumb; 
    console.log(bottom.childElementCount)
    if (bottom.childElementCount === 0){
            bottom.appendChild(deleteBtn);
        }
    else {};
        
    
    //delete button event listener that removes list items with a class of "done"
    deleteBtn.addEventListener("click", function() {
        Array.from(doneList.children).forEach(element => {
            console.log(element)
            if (element.className === "done") {
                element.remove(); 
            }
            //hide the delete button if the toDoArray is empty
            if (Array.from(doneList.children).length === 0) {
                let dumb = document.getElementById("deleteBtn");
                console.log(dumb);
                dumb.style.display = "none";
            }
        });
    });

    //display the delete button if the toDoArray  is populated
    // if (Array.from(doneList.children)) {
    //     let dumb = document.getElementById("deleteBtn");
    //     console.log(dumb);
    //     dumb.style.display = "block";
    // };


};

//event listener for the add submit-item button that starts the whole
let addItemButton = document.getElementById("submit-item");
addItemButton.addEventListener("click", addItem);



//UNUSED SORT METHOD, NOT OPTIMAL FOR REORGANIZING HTML ELEMENTS

// Array.from(webList.children).sort((a,b) => a.classList.contains("done")  - b.classList.contains("notDone"));
// let newOrder = Array.from(webList.children).sort(function(a,b){
//     console.log("test");
//     if (a.classList.contains("notDone") && b.classList.contains("done")){
//         console.log("test2");
//         return -1;}
//     if  (a.classList.contains("done") && b.classList.contains("done")){
//         return 1;}
//     return 0;
// });
// console.log(newOrder)