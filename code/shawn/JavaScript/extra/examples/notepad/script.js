// get elements from DOM
let newPost = document.getElementById("new-post");
let target = document.getElementById("target");
let submit = document.getElementById("submit");
let deleteSelectedButton = document.getElementById("delete-selected");

submit.addEventListener('click', function(event){
    // tell JS to prevent doing the normal default action (in this case, refreshing page after form submission)
    event.preventDefault();
    
    // get body of text
    let postBody = newPost.value;
    
    // create elements
    let div = document.createElement("section");
    let editButton = document.createElement("button");
    let deleteButton = document.createElement("button");
    let pTimeStamp = document.createElement("p");
    let pBody = document.createElement("p");
    let deleteCheckbox = document.createElement("input")

    // add classes
    div.classList.add("post");
    deleteButton.classList.add("button");
    editButton.classList.add("button")
    pBody.classList.add("post-text");
    pTimeStamp.classList.add("time-stamp");
    deleteCheckbox.classList.add("delete-checkbox");

    // set values
    editButton.innerText = "Edit Me";
    deleteButton.innerText = "Delete Me"
    pBody.innerText = postBody;
    pTimeStamp.innerText = new Date().toString();
    deleteCheckbox.type = "checkbox";


    // button event listeners
    deleteButton.addEventListener('click', function(){
        this.parentElement.remove();
    });
    editButton.addEventListener('click', function(){
            // get pBody text
            let bodyValue = pBody.innerText;
            // hide pBody
            pBody.style.display = "none";
            // create editable text area
            let editBox = document.createElement("textarea");
            // set starting value to stored pBody value
            editBox.value = bodyValue;
            // insert the editBox right where the pBody was
            div.insertBefore(editBox, pBody);
            // disable the edit button
            editButton.disabled = true;
            // create new button to save edits
            let saveButton = document.createElement("button");
            saveButton.innerText = "Save edits"
            div.insertBefore(saveButton, editButton);
            // add event listener to save button
            saveButton.addEventListener('click', function(){
                pBody.innerText = editBox.value;                // editBox is a textarea, so use .value.  pBody is a p, so use innerText
                pBody.style.display = "block";
                editButton.disabled = false;
                editBox.remove();
                saveButton.remove();
            });
    });

    // dadd elements to parent/page
    div.append(editButton);
    div.append(deleteButton);
    div.append(deleteCheckbox);
    div.append(pBody);
    div.append(pTimeStamp);
    target.insertBefore(div, target.firstChild);
});

deleteSelectedButton.addEventListener('click', function(){
    // look through target area only 
    let checkboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let box of checkboxes){
        if(box.checked){
            box.parentElement.remove();
        }
    }
});
styling, nested anonymous listening functions