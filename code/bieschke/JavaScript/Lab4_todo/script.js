let add = document.getElementById('addBtn'); 
let rem = document.getElementById('remove-all');

function newWorkout() {     //makes a new item
    let li = document.createElement('li');
    li.classList.add("incomplete")
    li.innerHTML = document.getElementById('addition').value;
    let inputValue = document.getElementById('addition').value;
    if (inputValue === ""){
        alert("No pain, no gain")
    } else {
    document.getElementById('items').appendChild(li);
    }

    document.getElementById("items").value = '';

    let span = document.createElement('span');
    span.innerHTML = document.getElementById('addition');

    for (i = 0; i < span.length; i++) {
        span[i].onclick = function() {
          let div = this.parentElement;
          div.style.display = "none";
        }
    }    
}

add.addEventListener('click', newWorkout)

//Checks an item as completed
let list = document.getElementById('items');
list.addEventListener('click', function(event){
  console.log(event.target)  
    if (event.target.className == 'incomplete') {
      event.target.className = 'complete';
      console.log("changed to complete")

    } else if (event.target.className == 'complete') {
        event.target.className = 'incomplete';
        console.log("changed to incomplete")      
    }
});

let allItems = document.getElementsByTagName('li')
let completedItems = document.getElementsByClassName('complete')
rem.addEventListener('click', deleteItems)

function deleteItems() {
  for (let i = 0; i < allItems.length; i++ ){
    if (allItems[i].className === 'complete'){
      allItems[i].remove()
    }
  }}