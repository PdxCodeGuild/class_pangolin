Vue.component('num', {
    props: ['number'], 
    template: `<div class="button" @click="$emit('inp', number)" > {{ number }} </div>`
});

Vue.component('op', {
    props: ['operator'], 
    template: `<div class="button operator" @click="$emit('op',operator)">{{ operator }}</div>` 
});


Vue.component('dis', {
    props: ['displaylogger'],
    template: `<div class="display">{{ displaylogger }}</div>`
});

Vue.component('ans', {
    props: ['displayanswer'],
    template: `<div class="answer">{{ displayanswer }}</div>`
});

let vm = new Vue({
  el: "#app",
  data() {
      return {
          evalList: "",
          current: "",
          answer: "",
          operatorClicked: true
      };
  },
  methods: {

    selectedNumber(number) {
        return number
    },

    selectedOperator(operator) {
        return operator
    },

    append(number) {
        if (this.operatorClicked == true) {
            this.current = "";
            this.operatorClicked = false;
        }
        this.selectedNumber(`${number}`);
        this.current = `${this.current}${number}`;
    },

    logger(operator) {
        if (this.operatorClicked == false) {
            this.evalList += `${this.current} ${operator} `;
            this.current = "";
            this.operatorClicked = true;
        }
    },

    addition() {
    this.selectedOperator("addition");
    this.logger("+");
    },

    subtraction() {
        this.selectedOperator("subtraction");
        this.logger("-");
    },

    multiply() {
        this.selectedOperator("multiply");
        this.logger("*");
    },
   
    divide() {
        this.selectedOperator("divide");
        this.logger("/");
    },

    clear() {
        this.selectedOperator("clear");
        this.current = "";
        this.answer = "";
        this.evalList = "";
        this.operatorClicked = false;
    },

    back() {
        this.selectedOperator("clear");
        this.current = "";
        this.answer = "";
    },

    sign() {
        this.selectedOperator("sign");
        if (this.current != "") {
            this.current = this.current.charAt(0) === "-" ? this.current.slice(1) : `-${this.current}`;
        }
    },

    percent() {
        this.selectedOperator("percent");
        if (this.current != "") {
            this.current = `${parseFloat(this.current) / 100}`;
        }
    },

    decimal() {
        this.selectedNumber("decimal");
        if (this.current.indexOf(".") === -1) {
            this.append(".");
        }
    },

    equal() {
        this.selectedOperator("equal");
        if (this.operatorClicked == false) {
            this.answer = eval(this.evalList + this.current);
        } 
    }
  }
});