let name = document.getElementById("name");
let email = document.getElementById("email");
let phone = document.getElementById("phone");
let birth = document.getElementById("birth");
let ssn = document.getElementById("ssn");
let username = document.getElementById("username");
let password = document.getElementById("password");
let results = document.getElementById("results");
let submit = document.getElementById("submit");

let arr=[]
submit.addEventListener('click', function(event){
    event.preventDefault();


    let Name = name.value;
    let Email = email.value;
    let Phone = phone.value;
    // let Birth = birth.value;
    let Ssn = ssn.value;
    let Username = username.value;
    let Password = password.value;

    let ptn_name = /.{3,}$/;
    let ptn_email = /[^@]+@[^\.]+\..+$/;
    let ptn_phone = /[0-9]{3}-[0-9]{3}-[0-9]{4}$/;
    // let ptn_birth = /^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$/;
    let ptn_ssn = /[0-9]{3}-[0-9]{2}-[0-9]{4}$/;
    let ptn_username = /^[a-zA-Z]\w{3,14}$/;
    let ptn_password = /^[a-zA-Z]\w{3,14}$/;

    let chk_name = Name.match(ptn_name);
    if (chk_name === null) {
        results.innerText = "Your user name does not match try again"
    } else {
        results.innerText = "Welcome " + chk_name
    }

    let chk_email = Email.match(ptn_email);
    if (chk_email === null){
        results.innerText = "Check your email agian"
    }

    let chk_phone = Phone.match(ptn_phone);
    if (chk_phone === null){
        results.innerText = "Check your phone number and try again"
    }

    // let chk_birth = Birth.match(ptn_birth);
    // console.log(chk_birth);
    // if (chk_birth === null){
    //     results.innerText = "Check your Birthday and try again"
    // }

    let chk_ssn = Ssn.match(ptn_ssn);
    if (chk_ssn === null){
        results.innerText = "Check your SSN and try again"
    }
    
    let chk_username = Username.match(ptn_username);
    if (chk_username === null){
        results.innerText = "Check your user name and try agian"
    }

    let chk_password = Password.match(ptn_password);
    if (chk_password === null){
        results.innerText = "Check your password and try agian"
    }

});


