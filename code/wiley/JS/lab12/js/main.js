/* Build a Calculator app.  
Should support numbers 0-9, a decimal place (.),
= (shows results)
+/- (negate the number)
% (percentage, dive by 100)
+-*\ (basic arithmatic)
backspace (to delete inputs)
Each button should be its own component. For many buttons, you cna use the same component.
HINT: you'll want to root 'data' attributes to store the current total, subtotal (screen display), and current operation. Some of you listener methods will change te total, some the subtotal, and some the operation. */

Vue.component('num',{
    props: ['number'],//props to be used for button value
    template: `
    <div class="btn" @click="$emit('inputnumber', number)" > {{ number }} </div>`, //template generates a div with an onclick listener that sends the parameters inputnumber(the onclick variable name, which then calls the Vue method numClick) and number(the prop)
});
Vue.component('oper',{
    props: ['operator'], //props for button value
    template: `
    <div class="btn operator" @click="$emit('operation',operator)">{{operator}}</div>
    `//template creates a div with the onclick listener that sends the parameters operation(the onclick variable name, which called the Vue method operClick) and operator(the prop)
}),
Vue.component('total',{
    props:['displaytotal'],
    template: `
    <div class="display">{{displaytotal}}</div>
    `
})


let vm = new Vue({
    el: '#Calculator',
    data:function() {
    return {
        number: 0,
        operator: "",
        total: 0,
        operationArray: []}
    },
    methods: {
        numClick: function(num){
            this.number += num
        },
        operClick: function(oper){
            this.operator = oper;
            if (this.operator === "AC"){
                this.operationArray = [],
                this.number = 0
                console.log(this.operationArray)
            }
            else if (this.operator === "="){
                this.operationArray.push(this.number)
                //parse through operationArray and complete operations.
                this.total = eval(this.operationArray)
                console.log(this.total)
                // this.operationArray = this.operationArray.map(x => parseFloat(x))
            }
            else {
                this.operationArray.push(this.number);
                this.operationArray.push(this.operator);
                // this.operationArray.push(this.operator);
                console.log(this.operationArray)
                this.number = "";}
        }


    },
    computed: {

    },
    mounted:function() {
        console.log("ITS ALIVE!")
    }
});