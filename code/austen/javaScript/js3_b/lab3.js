//impliment a crud repl
// //create, retrieve, update, delete
let create = document.getElementById("create").style.display = "none";
let crudl = document.getElementById("crudl");
let enter = document.getElementById("enter");
let find = document.getElementById("find");
let finder = document.getElementById("finder");
let who = document.getElementById("whoFind").style.display = "none";
let updateIt = document.getElementById("updateIt").style.display = "none";
let deleted = document.getElementById("deleted").style.display = "none";

let contact = [];

// enter.addEventListener('click', contact_new);

function contact_new(){
    var dict = {
        First: first.value,
        Last: last.value,
        Color: favcolor.value,  
    };
    // console.log("this is the contact_new", contact)
    contact.push(dict);
    console.log("this is push contact", contact);
    document.getElementById("create").style.display = "none";
}

function pushContact(){
    document.getElementById("create").style.display = "block";
    enter.addEventListener('click', contact_new);
}

function findem(){
    document.getElementById("whoFind").style.display = "block";
    go.addEventListener('click', lookup);
}

function lookup(){
    let lookup_question = document.getElementById("lookupQuestion").value;
    console.log(lookup_question)
    let findit = contact.filter(obj=>obj.First===lookup_question);
    let found = findit[0]
    let output = ''
    let foundKeys = Object.keys(found)
    let foundVals = Object.values(found)
    for (let i=0; i<foundKeys.length; i++){
        output += foundKeys[i] + " " + ":" + " "+ foundVals[i]+ "\n";
    };
    // console.log(findit);
    finder.innerText = output;
    document.getElementById("whoFind").style.display = "none";
}

function redo(){
    document.getElementById("updateIt").style.display = "block";
    new1.addEventListener('click', update);
}

function update(){
    let who = document.getElementById("who").value
    let what = document.getElementById("what").value
    let with_what = document.getElementById("with_what").value
    console.log(who,what,with_what)
    let new_val = contact.findIndex(obj=>obj.First === who);
    console.log("this is the new val ", new_val); // this finds who you what to update

    // contact[new_val].color = with_what;
    contact[new_val][what] = with_what; //this replaces the what with the with_what
    let newName = with_what;
    console.log('this is the new update', contact)
    // newUpdate.innerText = contact;
    let output = ''
    let foundKeys = Object.keys(contact[0])
    let foundVals = Object.values(contact[0])
    for (let i=0; i<foundKeys.length; i++){
        output += foundKeys[i] + " " + ":" + " "+ foundVals[i]+ "\n";
    };
    document.getElementById("updateIt").style.display = "none";
    // console.log(findit);
    newUpdate.innerText = "This is your updated contact: " + "\n" + output;
}

function thatsIt(){
    document.getElementById("deleted").style.display = "block";
    thatsAll.addEventListener('click', goodbye);
}

function goodbye(){
    let whoDelete = document.getElementById("later").value;
    let new_val = contact.findIndex(obj=>obj.First === whoDelete);
    
    delete contact[new_val]
    document.getElementById("deleted").style.display = "none";
    seeya.innerText = "You deleted: " + "\n" + whoDelete;
    console.log(contact);
}


let contact_list = true;
while (contact_list){
    let what_to_do = crudl.value
    if (what_to_do === 'c') {
        contact_new();
    }else if (what_to_do === 'f'){
        lookup();
    }else if (what_to_do === 'u'){
        update();
    }else if (what_to_do === 'd'){
        goodbye();
    }else {
        break
    }
}
c.addEventListener('click', pushContact);
f.addEventListener('click', findem);
u.addEventListener('click', redo);
d.addEventListener('click', thatsIt);
