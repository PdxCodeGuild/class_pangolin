class Account {
    constructor() {
        this.balance = 0;
        this.log = [[`Account created, balance is $${this.balance}`, new Date().toString()]];
    }
    updateTransactions(domLog) {
        // clear existing transaction
        domLog.innerHTML = '';

        for (let entry of this.log) {
            // create entry container, give class "transaction"
            let trans = document.createElement("div");
            trans.classList.add("transaction");

            // create two p tags going into the entry container, for date and message
            let pDate = document.createElement('p');
            let pMsg = document.createElement('p');
            pDate.classList.add('entry-date');
            pMsg.classList.add('entry-msg');

            // set values for pDate and pMsg
            pDate.innerText = entry[1];
            pMsg.innerText = entry[0];

            // add both to trans div
            trans.append(pDate);
            trans.append(pMsg);

            // add div to DOM's log
            domLog.append(trans);
        }
    }
    deposit(amount) {
        this.balance += parseFloat(amount);
        let log_str = `$${amount} was deposited.  New balance: $${this.balance}`;
        this.log.push([log_str, new Date().toString()]);
    }
    withdraw(amount) {
        this.balance -= amount;
        let log_str = `$${amount} was withdrawn.  New balance: $${this.balance}`;
        this.log.push([log_str, new Date().toString()]);
    }
}

function printResultMessage(p, result){
    if(result){
        p.innerText = "Success";
        p.hidden = false;
        p.setAttribute("style", `
            color: green;
        `);
    } else {
        p.innerText = "Denied";
        p.hidden = false;
        p.setAttribute("style", `
            color: red;
        `);  
    }
    // p.classList.add('fade-me');
}
// get DOM elements
let outputBalance = document.getElementById("output-balance");
let inputDeposit = document.getElementById("input-deposit");
let buttonDeposit = document.getElementById("button-deposit");
let messageDeposit = document.getElementById("message-deposit");
let inputWithdraw = document.getElementById("input-withdraw");
let buttonWithdraw = document.getElementById("button-withdraw");
let messageWithdraw = document.getElementById("message-withdraw");
let log = document.getElementById("log");

// setup account
account = new Account();
account.updateTransactions(log)

// event listeners: deposit
buttonDeposit.addEventListener('click', function () {
    let amount = inputDeposit.value;
    if (amount) {
        if (amount < 0) {
            let msg = "Deposit amount was less than or equal to zero...invalid transaction.";
            account.log.push([msg, new Date().toString()]);
            inputDeposit.value = '';
            printResultMessage(messageDeposit, false)
        } else {
            account.deposit(amount);
            inputDeposit.value = '';
            outputBalance.innerText = `$${account.balance}`;
            printResultMessage(messageDeposit, true)
        }
        account.updateTransactions(log);
    }
});
// event listeners: deposit
buttonWithdraw.addEventListener('click', function () {
    let amount = inputWithdraw.value;
    if (amount) {
        if (amount > account.balance) {
            let msg = 'Attempted to overdraft...transaction blocked.';
            // alert(msg)
            account.log.push([msg, new Date().toString()]);
            inputWithdraw.value = '';
            printResultMessage(messageWithdraw, false)
        }
        else if (amount < 0) {
            let msg = 'Attempted to withdraw negative amount...invalid transaction.';
            // alert(msg)
            account.log.push([msg, new Date().toString()]);
            inputWithdraw.value = '';
            printResultMessage(messageWithdraw, false)
        }
        
        else {
            account.withdraw(amount);
            inputWithdraw.value = '';
            outputBalance.innerText = `$${account.balance}`;
            printResultMessage(messageWithdraw, true)
        }
        account.updateTransactions(log);
    }
});

// event listener: on input, remove message
inputDeposit.addEventListener('input', function(){
    messageDeposit.hidden = true;
    messageWithdraw.hidden = true;
});
// event listener: on input, remove message
inputWithdraw.addEventListener('input', function(){
    messageWithdraw.hidden = true;
    messageDeposit.hidden = true;
});
