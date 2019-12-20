// declare variables with let, var, and const
// const cannot change value
// let only exists inside the function
// var is mutable

let newPost = document.getElementById("new-post");
let submit = document.getElementById("submit");
let target = document.getElementById("target");

submit.addEventListener('click', function(event) {
    event.preventDefault();
    let postBody = newPost.value;

    let div = document.createElement("section");
    // div.style.border = "1px solid black";
    // div.style.width = "640px";
    // div.style.minHeight = "160px";
    div.classList.add("post");

    let editButton = document.createElement("button");  //once a post is created, make an edit button
    let deleteButton = document.createElement("button");
    let pBody = document.createElement('p');
    let pTimeStamp = document.createElement('p');
    let deleteCheckBox = document.createElement('input');
    
    editButton.innerText = "Edit Me";
    editButton.addEventListener('click', function () {
        let bodyValue = pBody.innerText;
        pBody.style.display = "none";
        let editBox = document.createElement("textarea");
        editBox.value = bodyValue;
        editBox.style.display = "block";
        editBox.style.width = "100%";
        editBox.style.height = "auto";
        div.insertBefore(editBox, pBody);  

        editButton.disabled = true;

        let postButton = document.createElement('button');  //once the edit button is clicked, new options appear
        postButton.innerText = "Done Editing";
        postButton.addEventListener('click', function() {
            pBody.innerText = editBox.value;
            pBody.style.display = 'block';
            editBox.remove();
            editButton.disabled = false;
            postButton.remove();
        });

        div.insertBefore(postButton, editButton);

    });
    div.append(editButton);

    //let deleteButton = document.createElement("button");    //creates a button
    deleteButton.innerText = "Delete Me";    //label for the button
    deleteButton.addEventListener('click', function() {
        this.parentElement.remove()   //always there as a keyword to refer to self e.g. the deleteButton
    });                               //this.remove() would delete the deleteButton, the parentElement is the post
    div.append(deleteButton);

    p.innerText = postBody;
    div.append(pBody);

    pTimeStamp.innerText = new Date().toString();
    pTimeStamp.style.textAlign = "right";
    div.append(pTimeStamp);

    target.insertBefore(div, target.firstChild);    //puts the newest posts at the top

});

deleteSelectedButton.addEventListener('click', function() {
    let checkboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let i=0; i<)
});