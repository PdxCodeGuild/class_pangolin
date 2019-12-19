let newPost = document.getElementById("new-post");
let submit = document.getElementById("post");
let target = document.getElementById("target");
let deleteSelectedButton = document.getElementById("delete-selected");

// adds eventListener that listens for mouse click
submit.addEventListener('click', function(event) {
    // prevents page reload
    event.preventDefault();
    let postBody = newPost.value; 

    // creates new <div> + styling
    let div = document.createElement("section");
    div.style.border = "1px solid black";
    div.style.width = "640px";
    div.style.minWidth = "160px";
    div.style.wordWrap = "normal";

    let editButton = document.createElement("button")
    // creates deleteButton
    let deleteButton = document.createElement("button");
    // creates new <p>
    let pBody = document.createElement("p");
    // creates timestamp
    let pTimeStamp = document.createElement("p");
    // creates delete check box
    let deleteCheckBox = document.createElement("input");


    editButton.innerText = "Edit me";
    // listens for edit button click and then runs function
    editButton.addEventListener('click', function() {
        let bodyValue = pBody.value;
        pBody.style.display = "none";
        // creates text area when edit button is clicked
        editBox = document.createElement("textarea");
        editBox.value = bodyValue;
        editBox.style.display = "block";
        editBox.style.width = "100%";
        editBox.style.height = "auto";
        div.insertBefore(editBox, pBody);
        // turns off editButton after editing
        editButton.disabled = true 

        let postButton = document.createElement("button");
        postButton.innerText = "Done editing";
        postButton.addEventListener('click', function() {
            // puts editBox input inside pBody when Done editing button is clicked
            pBody.innerText = editBox.value;
            // turns pBody back into block rather than input
            pBody.style.display = "block";
            // removes editBox input
            editBox.remove();
            // turns editButton back on
            editButton.disabled = false;

        });
        div.insertBefore(postButton, editButton);

    });
    div.append(editButton);

    
    deleteButton.innerText = "Delete me";
    // function that deletes post when deleteButton is clicked
    deleteButton.addEventListener("click", function() {
        // specifies the parentElement of deleteButton
        this.parentElement.remove()
    });
    // adds deleteButton into div
    // div.append(deleteButton);

    deleteCheckBox.type = "checkbox";
    deleteCheckBox.classList.add("delete-checkbox");
    div.append(deleteCheckBox);

    
    pBody.innerText = postBody;
    div.append(pBody);

    
    // gives time as day/month/year/timezone
    pTimeStamp.innerText = new Date().toString();
    pTimeStamp.style.textAlign = "right";
    div.append(pTimeStamp);

    // arranges posts from news to oldest / top to bottom
    target.insertBefore(div, target.firstChild);

});

deleteSelectedButton.addEventListener('click', function() {
    let checkboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let i=0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkboxes[i].parentElement.remove()
        }
    }

});