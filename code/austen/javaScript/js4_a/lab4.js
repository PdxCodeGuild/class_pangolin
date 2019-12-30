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
