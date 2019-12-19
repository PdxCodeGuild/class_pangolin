let validInput = true;
// while (validInput) {

// }
function operation() {

    let validInput = true;
    while (validInput) {
        let operation_type = prompt("What operation would you like to preform? +, -, *, or /  ?  ");
        let first_num = parseFloat (prompt("What is your first number? "));
        let second_num = parseFloat (prompt("What is your second number? "));


        alert("Ok you would like to do "+ first_num + operation_type + second_num + ".");

        // let operation = operation_type;
        if (operation_type === '+') {
            alert("answer: "+ (first_num + second_num));
        }   else if (operation_type === '-') {
            alert("answer: " + (first_num - second_num));
        }   else if (operation_type === '*') {
            alert("answer: "+ (first_num * second_num));
        }   else if (operation_type === '/') {
            alert("answer: "+ (first_num / second_num));
        }   else {
                alert('please enter a valid responce: ')
        }
    }
}
operation();
