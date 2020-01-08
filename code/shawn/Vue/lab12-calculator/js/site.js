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
        <button @click="$emit('solve')" class="op-button" id="button-equal">=</button>
    `
});
Vue.component("decimal-button", {
    props: ['state'],
    template: `
        <button @click="$emit('decimal')" class="op-button" id="button-decimal" :disabled="state">dec</button>
    `
});
Vue.component("negate-button", {
    template: `
        <button @click="$emit('negate')" class="op-button" id="button-negate">neg</button>
    `
});
Vue.component("percent-button", {
    template: `
        <button @click="$emit('percent')" class="op-button" id="button-percent">%</button>
    `
});
Vue.component("clear-button", {
    template: `
        <button @click="$emit('clear')" class="op-button" id="button-clear">clear</button>
    `
});
Vue.component("back-button", {
    template: `
        <button @click="$emit('backspace')" class="op-button" id="button-back">backspace</button>
    `
});

let vm = new Vue({
    el: "#app",
    data: {
        subtotal: '0',              // the number you are currently typing
        numbers: [],                // the array of numbers and operators you've input
        currentOperation: '',       // the last operator you put in
        mode: 'start',              // the current mode....start, operation, and number
        decimalDisabled: false,     // a bool to help control behavior of adding decimal
        negateActive: false,        // a bool to help control behavior of negating number
        percentActive: false,       // a bool to help control behavior of percentages on number
        debug: false,               // a bool to control visibility of debug panel
    },
    methods: {
        inputNum: function (num) {
            // start mode...replace staring 0 with num
            if (this.mode === "start") {
                // this will replace starting 0
                if (this.negateActive) this.subtotal = '-' + num;
                else this.subtotal = num;
            }
            // operation mode...reset subtotal
            else if (this.mode === "operation") {
                this.subtotal = num;
            }
            // result mode....result all numbers
            else if (this.mode === "result") {
                this.numbers = [];
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
            }
            // result mode
            else if (this.mode === 'result') {
                this.numbers = [];
                this.numbers.push(parseFloat(this.subtotal));
                this.numbers.push(op);
            }
            else {
                this.numbers.push(parseFloat(this.subtotal))
                this.numbers.push(op);
            }
            this.mode = "operation";
            this.decimalDisabled = false;
            this.negateActive = false;
            this.percentActive = false;
        },
        doMath: function () {

            //order of operations:
            //parenthesis, exponents, multiplcation&division, addition&subtraction

            if (this.mode != 'result') {

                // add final number to expression, if not in operation mode
                if (this.mode != "operation") {
                    this.numbers.push(parseFloat(this.subtotal));
                } else {
                    // if we are in operation mode, then pop off the last operator before proceeding
                    this.numbers.pop();
                }
                // create copy of expression
                let result = [...this.numbers];

                console.log(`doing math`);
                // continue looping until expression is reduced to single number
                while (result.length > 1) {
                    console.log(`the results ${result}`)
                    // pemdas: exponents
                    for (let i = result.length - 1; i >= 0; i--) {
                        if (result[i] === "^") {
                            console.log(`${result[i - 1]}^${result[i + 1]}`)
                            result[i - 1] = result[i - 1] ** result[i + 1];
                            result.splice(i, 2);
                            i -= 2;
                        }
                    }
                    console.log(`the results ${result}`)
                    // pendas: multiplication and division
                    let loopCounter = result.length;
                    for (let i = 1; i < loopCounter; i++) {
                        if (result[i] === "×") {
                            console.log(`${result[i - 1]}*${result[i + 1]}`)
                            result[i - 1] = result[i - 1] * result[i + 1];
                            result.splice(i, 2);
                            i--;
                            loopCounter -= 2;
                        } else if (result[i] === "÷") {
                            console.log(`${result[i - 1]}/${result[i + 1]}`)
                            result[i - 1] = result[i - 1] / result[i + 1];
                            result.splice(i, 2);
                            i--;
                            loopCounter -= 2;
                        }
                    }
                    console.log(`the results ${result}`)
                    // pemdas: addition and subtraction
                    for (let i = 1; i < result.length; i++) {
                        if (result[i] === "+") {
                            console.log(`${result[i - 1]}+${result[i + 1]}`)
                            result[i - 1] = result[i - 1] + result[i + 1];
                            result.splice(i, 2);
                            i--;
                            loopCounter -= 2;
                        } else if (result[i] === "-") {
                            console.log(`${result[i - 1]}-${result[i + 1]}`)
                            result[i - 1] = result[i - 1] - result[i + 1];
                            result.splice(i, 2);
                            i--;
                            loopCounter -= 2;
                        }
                    }

                    console.log(`the results ${result}`)
                }
                console.log(`${this.numbers} reduces to ${result}`)

                // do some things to finalize this caluculation
                this.numbers.push('=', result[0])                       // push result so it's desplayed with expression
                this.subtotal = result[0];                              // update working number with result
                this.mode = 'result';                                   // set mode to result
                this.decimalDisabled = false;                           // reset decimal
                this.negateActive = false;                              // reset negate
                this.percentActive = false;                             // reset percent
            }
        },
        addDecimal: function () {
            // start mode...replace staring 0 with num
            if (this.mode === "start") {
                // this will add decimal to existing 0
                this.subtotal = '0.';
            }
            // operation mode...reset subtotal
            else if (this.mode === "operation") {
                this.subtotal = '0.';
            }
            // number input mode...concat
            else {
                this.subtotal += '.';
            }
            // set mode to number
            this.mode = 'number';
            this.decimalDisabled = true;
        },
        toggleNegate: function () {
            if (this.negateActive) {
                this.subtotal = this.subtotal.replace('-', '');
            } else {
                this.subtotal = '-' + this.subtotal;
            }
            this.negateActive = !this.negateActive;
        },
        togglePercent: function () {
            if (this.percentActive) {
                this.subtotal = (parseFloat(this.subtotal) * 100).toString();
            } else {
                this.subtotal = (parseFloat(this.subtotal) / 100).toString();
            }
            this.percentActive = !this.percentActive;
        },
        clear: function () {
            this.subtotal = '0';
            this.numbers = [];
            this.currentOperation = '';
            this.mode = 'start';
            this.decimalDisabled = false;
            this.negateActive = false;
            this.percentActive = false;
        },
        backspace: function () {
            this.subtotal = this.subtotal.slice(0, -1)
        }
    },
    computed: {
        prettyEquation: function () {
            return this.numbers.join(" ");
        }
    },
    mounted: function () {
        // number event listener: keyboard
        window.addEventListener('keydown', function (event) {
            console.log(`keypress: ${event.key}`)
            let input = event.key;
            if ('0123456789'.includes(input)) vm.inputNum(input);
            if ('+-^'.includes(input)) vm.operate(input);
            if (input === '/') vm.operate('÷');
            if (input === '*') vm.operate('×');
            if (input === '=' || input === 'Enter') vm.doMath();
            if (input === '.') vm.addDecimal();
            if (input === 'Backspace') vm.backspace();
            if (input === 'd') vm.debug = !vm.debug;
        });
    }
});