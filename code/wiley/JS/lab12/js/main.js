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
Vue.component('backspace',{
    props:['backspace'],
    template:
    `<div class="btn" @click="$emit('backspace', backspace)" > {{ backspace }} </div>`
})


let vm = new Vue({
    el: '#Calculator',
    data:function() {
    return {
        number: '',
        current: '',
        total: '',
        operator: "",
        operation: "",
        display: 0,}
    },
    methods: {
        backSpaceClick: function(num){
            this.number = this.number.substring(0, this.number.length -1)
            this.display = this.number
            this.current = this.number
        },
        numClick: function(num){
            // if (num === '.'){
            //     if (this.number.indexOf('.')===-1){
            //     this.number 
            //     console.log("testing this shit")
            // }}
                this.number += num 
                this.current = this.number
                this.display = this.current
            
            },
            operClick: function(oper){
                this.operator = oper; //gets the operator payload
                
                if (this.operator === "AC"){ //works
                    this.operation = "",
                    this.number = "",
                    this.total = "",
                    this.current = ""
                    this.display = 0
            }
            
            else if (this.operator === "+/-"){ //works
                this.current = parseFloat(this.current)
                this.current *= -1
                this.total = this.current
                this.display = this.current

            }
            else if (this.operator === "%") {
                this.current = parseFloat(this.current)
                this.current /= 100
                this.display = this.current


            }
            else if (this.operator === "="){
                // console.log("this is the operation" + this.operation)
                if (this.operation === "+"){
                    console.log("Num Click Console Test = ", this.current +" <-current number -> "+  this.number);
                    this.total = parseFloat(this.current) + parseFloat(this.total)
                    console.log("hello sarah")
                    this.current = this.total
                    this.display = this.current
                }
                else if (this.operation === "-"){
                    console.log("total is " + this.total, "number is " + this. current)
                    this.total = parseFloat(this.total) - parseFloat(this.current)
                    this.current = this.total
                    this.display = this.current

                    
                }
                else if (this.operation === "*"){
                    console.log("total is " + this.total, "number is " + this. number)
                    this.total = parseFloat(this.total) * parseFloat(this.current)
                    this.current = this.total
                    this.display = this.current

                    
                }
                else if (this.operation === "/"){
                    console.log("total is " + this.total, "number is " + this. number)
                    this.total = parseFloat(this.total) / parseFloat(this.current)
                    this.current = this.total
                    this.display = this.current

                    
                }
                else {
                    this.current = "ERROR"
                }
                
                // this.number = "";
            }
            else {
                this.total = this.current;
                this.current = this.number
                console.log(this.number + "  is this right?")
                this.number = '';
                this.operation = oper
                this.display+=this.operation
                console.log("Num Click Console Test = ", this.current +" <-current number -> "+  this.number);
                // this.number = "";}
            }}
            
            
        },
        computed: {
            
        },
        mounted:function() {
            console.log("ITS ALIVE!")
        }
    });