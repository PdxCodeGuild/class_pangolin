let username = document.getElementById("username");
let password = document.getElementById("password");
let first_name = document.getElementById("first_name");
let last_name = document.getElementById("last_name");
let email = document.getElementById("email");
let phone = document.getElementById("phone");
let dob = document.getElementById("dob");
let ssn = document.getElementById("ssn");
let submit = document.getElementById("submit");
let results = document.getElementById("results");


submit.addEventListener('click', function(event) {
    event.preventDefault()
    let userName = username.value; //^[a-zA-Z0-9]{6,}$
    let passWord = password.value;
    let firstName = first_name.value; //^[a-zA-Z\s]{3,}$
    let lastName = last_name.value;
    let eMail = email.value; //[^@]+@[^\.]+\..+
    let phoneNum = phone.value; //^[1-9]{3}-[0-9]{3}-[0-9]{4}$
    let dOb = dob.value; //^[0-1]{1}[0-9]{1}\/[0-3]{1}[0-9]{1}\/[0-2]{1}[0]{1}[0-2]{1}[0-9]{1}$
    let SSN = ssn.value; //^[0-9]{3}-[0-9]{2}-[0-9]{4}$

    let pat_un = /^[a-zA-Z0-9]{6,}$/;
    let pat_pw = /^.{6,}$/;
    let pat_fN = /^[a-zA-Z\s]{2,}$/;
    let pat_lN = /^[a-zA-Z\.\s]{3,}$/;
    let pat_em = /[^@]+@[^\.]+\..+/;
    let pat_pn = /^[1-9]{3}-[0-9]{3}-[0-9]{4}$/;
    let pat_dob = /^[0-9]{2}\/[0-9]{2}\/[0-9]{2,4}$/;
    let pat_ssn = /^[0-9]{3}-[0-9]{2}-[0-9]{4}$/;

    let Result_un = userName.match(pat_un);
    if (Result_un == null) {
        results.innerText = 'Your username must be Alphanumeric (no symbols) and 6 or more characters.';
    } else {
        results.innerText = `Welcome ${Result_un}!`;
    }

    let Result_pw = passWord.match(pat_pw);
    if (Result_pw == null) {
        results.innerText = 'Your password must be 6 characters or more.';
    }

    let Result_fN = firstName.match(pat_fN);
    if (Result_fN == null) {
        results.innerText = 'Your first/given name must be Alpha only and more than 6 characters.';
    }

    let Result_lN = lastName.match(pat_lN);
    if (Result_lN == null) {
        results.innerText = 'Your last/family name must be Alphanumeric and more than 6 characters.';
    }

    let Result_em = eMail.match(pat_em);
    if (Result_em == null) {
        results.innerText = 'Your email needs to be corrected.';
    }

    let Result_pn = phoneNum.match(pat_pn);
    if (Result_pn == null) {
        results.innerText = 'Your phone number needs to be corrected.';
    }

    let Result_dob = dOb.match(pat_dob);
    if (Result_dob == null) {
        results.innerText = 'Your date of birth needs to be in mm/dd/yyyy format.';
    }

    let Result_ssn = SSN.match(pat_ssn);
    if (Result_ssn == null) {
        results.innerText = 'Your SSN needs to be corrected.';
    }
});