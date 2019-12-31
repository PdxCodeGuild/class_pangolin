let userArray = []; // User input array
let total = 0; // Variable initialization for summing user array values

let number_inp = document.querySelector('#number_inp');
let submit_btn = document.querySelector('#submit_btn');
let output_div = document.querySelector('#output_div');

submit_btn.onclick = function() {
 
    userArray.push(parseInt(name_input.value));
    total = userArray.reduce((a, b) => a + b, 0);
    output_div.innerText = total / userArray.length;
}
