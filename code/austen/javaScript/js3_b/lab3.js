//impliment a crud repl
// //create, retrieve, update, delete
let create = document.getElementById("create").style.display = "none";
let crudl = document.getElementById("crudl");
let enter = document.getElementById("enter");
let find = document.getElementById("find");


let contact = [];

// enter.addEventListener('click', contact_new);

function contact_new(){
    var dict = {
        first: first.value,
        last: last.value,
        color: favcolor.value,  
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

function lookup(){
    let lookup_question = prompt('Who would you like to lookup? ');
    let findit = contact.filter(obj=>obj.first===lookup_question);
    // document.write(findit);
    console.log(findit);
}
// lookup();

function update(){
    let who = prompt('Who would you like to update?');
    let what = prompt('What would you like to update? first, last, color?');
    let with_what = prompt('What do you want to update it with?');

    let new_val = contact.findIndex(obj=>obj.first === who);
    console.log("this is the new val ", new_val); // this finds who you what to update

    // contact[new_val].color = with_what;
    contact[new_val][what] = with_what; //this replaces the what with the with_what
    console.log('this is the new update', contact[new_val])
}

function goodbye(){
    let whoDelete = prompt('Who would you like to delete?');
    let new_val = contact.findIndex(obj=>obj.first === whoDelete);
    
    delete contact[new_val]
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
f.addEventListener('click', lookup);
u.addEventListener('click', update);
d.addEventListener('click', goodbye);
