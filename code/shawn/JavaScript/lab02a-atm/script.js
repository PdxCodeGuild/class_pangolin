class Account{
    constructor(){
        this.balance = 0;
        this.log = [`Account created, balance is $${this.balance}`];
    }
    print_transactions(){
        return this.log.join('\n');
    }
    deposit(amount){
        if(amount < 0) {
            alert("Deposit amount was less than or equal to zero...no changes made.")
            this.log.push('Attempted to deposit negative number...transaction blocked.')
        } else {
            console.log(amount);
            this.balance += amount;
            let log_str = `$${amount} was deposited.  New balance: $${this.balance}`;
            this.log.push(log_str);
            alert(log_str);
        }
    }
    withdraw(amount){
        if(this.balance - amount < 0){
            alert(`Overdraft protection...too large of a withdraw, no action taken.`);
            this.log.push('Attempted to overdraft...transaction blocked.')
        } else {
            this.balance -= amount;
            let log_str = `$${amount} was withdrawn.  New balance: $${this.balance}`;
            this.log.push(log_str);
            alert(log_str);
        }
    }
}

account = new Account();

//repl loop
let run_flag = true
while (run_flag){
    let command = prompt("What would you like to do? \n(d) - deposit \n(w) - withdraw\n(c) - check balance\n(s) - show transaction history\n(q) quit\nYour input: ");
    // quit
    if (command === 'q'){
        alert("quitting");
        run_flag = false;
    } 
    // deposit
    else if (command === 'd'){
        let user_input = prompt("Enter amount to deposit: ");
        account.deposit(parseFloat(user_input));
    } 
    // withdraw
    else if (command === 'w'){
        let user_input = prompt("Enter amount do withdraw: ");
        account.withdraw(parseFloat(user_input));
    } 
    // check balance
    else if (command === 'c'){
        alert(`Account balance: $${account.balance}`);
    }
    // show transaction history
    else if (command === 's'){
        alert(`Transaction history:\n ${account.print_transactions()}`);
    } 

}
