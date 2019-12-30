class Account {
    constructor(money=0) {
        this.money = money;
        this.transactions = '';
        this.transactionList = [];
    }

    balance() {
        return this.money;
    }

    deposit() {
        this.money += deposit;
        this.transactions = `User deposited ${this.money}`
        this.transactionList.push(this.transactions)
    }

    checkWithdrawal(withdraw) {
        if (this.money >= withdraw) {
            return true;
        } else {
            return false;
        }
    }

    withdraw() {
        if (this.checkWithdrawal(this.money) === true) {
            this.money -= withdraw;
            this.transactions = `User withdrew ${withdraw}`;
            this.transactionList.push(this.transactions);
        } else {
            console.log("I\'m sorry Dave, I can\'t do that. Insufficient funds.")
        }
    }

    printTransactions() {
        return this.transactionList
    }

}

b = new Account();
lions = true;
while (lions === true) {
    let action = prompt("You can deposit, withdraw, check balance, or history, or enter q or 1 to quit.\n>")

    if (action.includes('d', 'deposit')) {
        deposit = Number(prompt("How much would you like to deposit?\n> "));
        b.deposit();
    } else if (action.includes('w', 'withdraw')) {
        withdraw = Number(prompt("How much would you like to withdraw?\n> "));
        b.withdraw();
    } else if (action.includes('c', 'check')) {
        alert("Today we check your balance!");
        alert(b.balance());
    } else if (action.includes('h', 'history')) {
        alert("Today we check history!");    
        alert(b.printTransactions());
    } else if (action.includes('q', '1')) {
        alert("Sayonara!");
        return b.deposit();
    }
}   