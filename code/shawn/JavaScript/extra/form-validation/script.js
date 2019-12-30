// get DOM objects
let username = document.getElementById("username");
let usernameMsg = document.getElementById("username-msg")
let password = document.getElementById("password");
let passwordMsg = document.getElementById("password-msg")
let name = document.getElementById("name");
let nameMsg = document.getElementById("name-msg")
let email = document.getElementById("email");
let emailMsg = document.getElementById("email-msg")
let phone = document.getElementById("phone");
let phoneMsg = document.getElementById("phone-msg")
let birthday = document.getElementById("birthday");
let birthdayMsg = document.getElementById("birthday-msg")
let ssn = document.getElementById("ssn");
let ssnMsg = document.getElementById("ssn-msg")
let submit = document.getElementById("submit");

// boolean variable for enabling submit button
let formIsValid = false;
let usernameIsValid = false;
let passwordIsValid = false;
let nameIsValid = false;
let emailIsValid = false;
let phoneIsValid = false;
let birthdayIsValid = false;
let ssnIsValid = false;

function checkForm() {
    if (usernameIsValid && passwordIsValid && nameIsValid && emailIsValid && phoneIsValid && birthdayIsValid && ssnIsValid){
        submit.disabled = false;
        submit.style.color = "rgb(0,128,0)";

    } else {
        submit.disabled = true;
        submit.style.color = "rgba(255,0,0,.3)";
    }
}

// event listeners
username.addEventListener("input", function () {
    let regex = /[\w]{6,}/i;
    let match = regex.exec(username.value);
    if (match) {
        usernameMsg.style.color = "green";
        usernameIsValid = true;
    } else {
        usernameMsg.style.color = "red";
        usernameIsValid = false;
    }
    checkForm();
});
password.addEventListener("input", function () {
    let regex = /[A-Za-z0-9!@#$%^&*()_,.]{6,}/i;
    let match = regex.exec(password.value);
    if (match) {
        passwordMsg.style.color = "green";
        passwordIsValid = true;
    } else {
        passwordMsg.style.color = "red";
        passwordIsValid = false;
    }
    checkForm();
});
name.addEventListener("input", function () {
    let regex = /[A-Za-z]{1,} [A-Za-z]{1,}/i;
    let match = regex.exec(name.value);
    if (match) {
        nameMsg.style.color = "green";
        nameIsValid = true;
    } else {
        nameMsg.style.color = "red";
        nameIsValid = false;
    }
    checkForm();
});
email.addEventListener("input", function () {
    let regex = /[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+/i;
    let match = regex.exec(email.value);
    if (match) {
        emailMsg.style.color = "green";
        emailIsValid = true;
    } else {
        emailMsg.style.color = "red";
        emailIsValid = false;
    }
    checkForm();
});
phone.addEventListener("input", function () {
    let regex = /\d{3}-\d{3}-\d{4}/i;
    let match = regex.exec(phone.value);
    if (match) {
        phoneMsg.style.color = "green";
        phoneIsValid = true;
    } else {
        phoneMsg.style.color = "red";
        phoneIsValid = false;
    }
    checkForm();
});
birthday.addEventListener("input", function () {
    let regex = /\d+\/\d+\/\d{4}/i;
    let match = regex.exec(birthday.value);
    if (match) {
        birthdayMsg.style.color = "green";
        birthdayIsValid = true;
    } else {
        birthdayMsg.style.color = "red";
        birthdayIsValid = false;
    }
    checkForm();
});
ssn.addEventListener("input", function () {
    let regex = /\d{3}-\d{2}-\d{4}/i;
    let match = regex.exec(ssn.value);
    if (match) {
        ssnMsg.style.color = "green";
        ssnIsValid = true;
    } else {
        ssnMsg.style.color = "red";
        ssnIsValid = false;
    }
    checkForm();
});