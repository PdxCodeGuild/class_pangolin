// declare variables with let, var, and const
// const cannot change value
// let only exists inside the function
// var is mutable

let newPost = document.getElementById("new-post");
let submit = document.getElementById("submit");
let target = document.getElementById("target");

submit.addEventListener('click', function() {
    event.preventDefault();
    let postBody = newPost.value;

    let div = document.createElement("section");
    div.style.border = "1px solid black";
    div.style.width = "640px";
    div.style.minHeight = "160px"

    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete Me"

    div.append(deleteButton);

    let p = document.createElement("p");
    p.innerText = postBody;
    div.append(pBody);

    let pTimeStamp = document.createElement("p");
    pTimeStamp.innerText = new Date().toString();
    pTimeStamp.style.textAlign = "right";
    div.append(pTimeStamp);

    target.append(div);

});