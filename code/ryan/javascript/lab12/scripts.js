Vue.component('operator', {
    props: ['op'],
    template: `
    <div class="col-3">
    <button v-on:click="$emit('input', op)" class="btn btn-block bg-warning my-3">{{ op }}</button>
    </div>    
    `
});

Vue.component('number', {
    props: ['num'],
    template: `
    <div class="col-3">
    <button v-on:click="$emit('input', num)" class="btn btn-block bg-secondary my-3">{{ num }}</button>
    </div>    
    `
});



let vm = new Vue({
    el: '#calculator',
    data: {
        inputDisplay: "",
        firstNum: "",
        secondNum: "",
        operator: null,
        operatorClicked: false
        
    },
    methods: {
        numList: function(num) {
            if (this.operatorClicked) {
                this.inputDisplay = '';
                this.operatorClicked = false;
            }
            this.inputDisplay += (`${num}`);
        },
        clear: function() {
            this.inputDisplay = "";
        },
        posNeg: function() {
            if (this.inputDisplay.charAt(0) === "-") {
                this.inputDisplay = this.inputDisplay.slice(1);
            } else {
                this.inputDisplay = `-${this.inputDisplay}`;
            }
        },
        percent: function() {
            this.inputDisplay = `${parseFloat(this.inputDisplay) / 100}`;
        },
        back: function() {
            this.inputDisplay = this.inputDisplay.substring(0, this.inputDisplay.length - 1);
        },
        dot: function() {
            if (this.inputDisplay.indexOf('.') === -1) {
                this.inputDisplay += '.';
            }
        },
        setFirstNum: function() {
            this.firstNum = this.inputDisplay;
            this.operatorClicked = true;
        },
        add: function() {
            this.operator = (a, b) => a + b;
            this.setFirstNum();
        },
        minus: function() {
            this.operator = (a, b) => a - b;
            this.setFirstNum();
        },
        multiply: function() {
            this.operator = (a, b) => a * b;
            this.setFirstNum();
        },
        divide: function() {
            this.operator = (a, b) => a / b;
            this.setFirstNum();
        },
        equals: function() {
            this.inputDisplay = this.operator(
                parseFloat(this.firstNum),
                parseFloat(this.inputDisplay)
            );
        },
    }
}); 