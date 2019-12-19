//impliment a crud repl
// //create, retrieve, update, delete


let contact = [];

function contact_new(){
    // let question = prompt('Would you like to add a contact? ');
    // if (question === 'yes'){
    var dict = {
        first: prompt('What is your first name? '),
        last: prompt('What is your last name? '),
        color: prompt('What is your favorite color? '),
    };
    contact.push(dict);
        // return dict;
    
}
// contact.push(dict);
// contact.push(contact_new());
console.log(contact);

function lookup(){
    let lookup_question = prompt('Who would you like to lookup? ')
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
        
    //     console.log(newnew);
    //     // Remove item
    //     delete contact.value;
    // console.log();
    // let updated_val = new_val[0].what = with_what;
    // console.log(updated_val);


let contact_list = true;
while (contact_list){
    let what_to_do = prompt('What would you like to do? c, f, u, d, done')
    if (what_to_do === 'c') {
        contact_new();
    }else if (what_to_do === 'f'){
        lookup();
    }else if (what_to_do === 'u'){
        update();
    }else if (what_to_do === 'd'){
        goodbye();
    }else {
        alert('Ok see your next time!')
        break
    }
}


