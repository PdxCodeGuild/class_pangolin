Vue.component("number-button", {
    props: ['number'],
    template: `
        <button @click="$emit('number-input',number)" class="num-button" v-bind:id="'button-' +  number">{{number}}</button>
    `
});
Vue.component("operation-button", {
    props: ['operation', 'symbol'],
    template: `
        <button @click="$emit('operation-input', symbol)" class="op-button" v-bind:id="'button-' + operation">{{symbol}}</button>
    `
});
Vue.component("equals-button", {
    template: `
        <button @click="$emit('solve')" class="eq-button" id="button-equal">=</button>
    `
});

let vm = new Vue({
    el: "#app",
    data: {
        equation: '',
        total: 0,
        subtotal: '0',
        numbers: [],
        currentOperation: '',
        mode: 'start',
    },
    methods: {
        inputNum: function (num) {
            // start mode...replace staring 0 with num
            if (this.mode === "start") {
                // this will replace starting 0
                this.subtotal = num;
            }
            // operation mode...reset subtotal
            else if (this.mode === "operation") {
                this.subtotal = num;
            }
            // number input mode...concat
            else {
                this.subtotal += num.toString();
            }
            // set mode to number
            this.mode = 'number';
        },
        operate: function (op) {

            // operation mode...just change operation
            if (this.mode === 'operation') {
                this.numbers.pop();
                this.numbers.push(op);
            } else {
                this.numbers.push(parseFloat(this.subtotal))
                this.numbers.push(op);
            }
            this.mode = "operation";
        },
        doMath: function () {
            //order of operations:
            //parenthesis, exponents, multiplcation, division, addition, subtraction

            // add final number to expression
            this.numbers.push(parseFloat(this.subtotal))
            // create copy of expression
            let result = [...this.numbers];

            console.log(`doing math`);
            // continue looping until expression is reduced to single number
            while (result.length > 1) {
                console.log(`the results ${result}`)
                // pemdas: exponents
                for (let i = result.length - 1; i >= 0; i--) {
                    if (result[i] === "**") {
                        console.log(`${result[i - 1]}**${result[i + 1]}`)
                        result[i - 1] = result[i - 1] ** result[i + 1];
                        result.splice(i, 2);
                        i -= 2;
                    }
                }
                console.log(`the results ${result}`)
                // pendas: multiplication
                for (let i = result.length - 1; i >= 0; i--) {
                    if (result[i] === "×") {
                        console.log(`${result[i - 1]}*${result[i + 1]}`)
                        result[i - 1] = result[i - 1] * result[i + 1];
                        result.splice(i, 2);
                        i -= 2;
                    }
                }
                console.log(`the results ${result}`)
                // pemdas: division
                for (let i = result.length - 1; i >= 0; i--) {
                    if (result[i] === "÷") {
                        console.log(`${result[i - 1]}/${result[i + 1]}`)
                        result[i - 1] = result[i - 1] / result[i + 1];
                        result.splice(i, 2);
                        i -= 2;
                    }
                }
                console.log(`the results ${result}`)
                // pemdas: addition
                for (let i = result.length - 1; i >= 0; i--) {
                    if (result[i] === "+") {
                        console.log(`${result[i - 1]}+${result[i + 1]}`)
                        result[i - 1] = result[i - 1] + result[i + 1];
                        result.splice(i, 2);
                        i -= 2;
                    }
                }
                console.log(`the results ${result}`)
                // pemdas: subtraction
                for (let i = result.length - 1; i >= 0; i--) {
                    if (result[i] === "-") {
                        console.log(`${result[i - 1]}-${result[i + 1]}`)
                        result[i - 1] = result[i - 1] - result[i + 1];
                        result.splice(i, 2);
                        i -= 2;
                    }
                }
                console.log(`the results ${result}`)
            }
            console.log(`${this.numbers} reduces to ${result}`)
        }
    }
});