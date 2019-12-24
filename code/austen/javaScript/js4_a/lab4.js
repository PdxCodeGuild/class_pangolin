let submit = document.getElementById("first");
let target = document.getElementById("target");
let deleteIt = document.getElementById("deleteIt")
let moveIt = document.getElementById("moveIt")
let done = document.getElementById("done")

submit.addEventListener('click', function(e){
    e.preventDefault();
    let post = newPost.value;

    let div = document.createElement("todo");
    div.classList.add("new");

    let postBody = document.createElement("li");
   
    postBody.innerText = post;
    div.append(postBody);
    
    let pTimeStamp = document.createElement('p');
    pTimeStamp.innerText = new Date().toString();
    // pTimeStamp.style.textAlign = "right";
    pTimeStamp.style.textDecoration = "underline";
    div.append(pTimeStamp);

    let deleteCheckBox = document.createElement("input");
    deleteCheckBox.type = "checkbox";
    deleteCheckBox.classList.add("delete-checkbox");
    div.append(deleteCheckBox);

    document.getElementById("newPost").value = '';
  
    target.insertBefore(div, target.firstChild);

    // let postValue = postBody.innerText;
    // postBody.style.display = "none";

});

deleteIt.addEventListener('click', function(){
    let checkboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let i=0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkboxes[i].parentElement.remove()
        } 
    }
});

moveIt.addEventListener('click', function(){
    let moveboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let i=0; i < moveboxes.length; i++) {
        if (moveboxes[i].checked) {
            let move = document.createElement("p")
            move = moveboxes[i].parentElement
            move.style.textDecoration = "line-through";
            done.append(move)
        }
    }

});



// let add = document.getElementById("add");
// let listItems = document.getElementById("listItems").style.display = "none";
// let deleteIt = document.getElementById("deleteIt");
// let target = document.getElementById("target");



// add.addEventListener("click", function(event){
//     event.preventDefault();
//     // let ul = document.getElementById("item");
//     // let li = document.createElement("li");
//     // let deleteButton = document.createElement("button");

//     let div = document.createElement("section");
//     div.classList.add("post");


//     let checkbox = document.createElement("input");
//     checkbox.type = "checkbox";
//     checkbox.classList.add("delete-checkbox");
//         // checkbox.id = "items";
    
//         //this appends checkbox to li
        
//         let firstItem = document.getElementById("first");
//         //this appends the typed in val to li
//         div.append(checkbox);
//         div.append(firstItem);


//         // li.appendChild(document.createTextNode(firstItem.value));
//         // this appends everything added to the ul
//         // ul.appendChild(li)
        
//         //this shows all
//         document.getElementById("listItems").style.display = "block";
        
//         console.log(ul)
//         console.log(li)
//         //this resets the value in the text box to nothing
//         document.getElementById("first").value = '';
        
//         // target.insertBefore(li, target.firstChild);
//         console.log("parernt",checkbox.parentElement)

//         target.insertBefore(div,target.firstChild);
//     });
    
//     deleteIt.addEventListener('click', function() {
//         let checkedOff = li.querySelectorAll("input[type='checkbox'].delete-checkbox");
//     console.log("this is ", checkedOff);
//         if (checkedOff.checked === true) {
//             alert("checked")
//             checkedOff.parentElement.remove()
//         }else {
//             delete(ul)
//             alert("ugh")
//         }
    
// });
