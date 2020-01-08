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
        number: '',
        current: '',
        operator: "",
        total: 0,
        operation: ""}
    },
    methods: {
        numClick: function(num){
            //check for multiple . not currently in operation
            // if (this.number[this.number.length-1] === "."){
            //     this.number.slice(-1)
            //     console.log("testing splice  " + this.number)
            // }
            this.number += num
            this.total = this.number
            console.log("Num Click Console Test = ", this.number +" <-number total -> "+  this.total)
        },
        operClick: function(oper){
            this.operator = oper;
            console.log(this.current)
            this.total = this.current;
            this.current = this.number;
            this.number = '';
            console.log("Num Click Console Test = ", this.current +" <-current total -> "+  this.total);
            console.log(this.operator)
           

            if (this.operator === "AC"){ //works
                this.operation = "",
                this.number = "",
                this.total = ""
            }
            
            else if (this.operator === "+/-"){ //works
                this.number = parseFloat(this.number)
                this.number *= -1
                this.total = this.number
            }
            else if (this.operator === "="){
                console.log("this is the operation" + this.operation)
                if (this.operation === "+"){
                    this.number2 = this.number
                    this.total = parseFloat(this.current) + parseFloat(this.total)
                    console.log(isNaN(this.total))
                    this.current = this.total
                }
                else if (this.operation === "-"){
                    console.log("total is " + this.total, "number is " + this. number)
                    this.total = parseFloat(this.total) - parseFloat(this.current)
                    this.current = this.total

                }
                else if (this.operation === "*"){
                    console.log("total is " + this.total, "number is " + this. number)
                    this.total = parseFloat(this.total) * parseFloat(this.current)
                    this.current = this.total

                }
                else if (this.operation === "/"){
                    console.log("total is " + this.total, "number is " + this. number)
                    this.total = parseFloat(this.total) / parseFloat(this.current)
                    this.current = this.total

                }
                else {
                    this.total = "ERROR"
                }
                
                // this.number = "";
            }
            else {
                this.operation = oper
            }
        },
        percentClick: function(num){ //works
            console.log(this.number)
            this.number = parseFloat(this.number);
            this.number /= 100;
            this.total = this.number;
            this.number = "";
        },
        


    },
    computed: {

    },
    mounted:function() {
        console.log("ITS ALIVE!")
    }
});



//trash
// this.operationArray.push(this.number);
                // this.operationArray.reduce(function(a,b){
                //     if (this.operationArray.length >= 3){
                //         console.log("this is running?")
                //         return this.operationArray[a[1]](parseFloat(a[0]),(parseFloat(a[2])));
                //     } else {
                //         console.log(a)
                //         return a.push(b)}
                // })
                //parse through operationArray and complete operations.
                // this.total = eval(this.operationArray)
// addClick: function(num){
    
//     this.number = (a,b) => a+b;
// },
// subractClick: function(a,b) {
//     this.number = (a-b)
// },
// divideClick:function(a,b) {
//     this.number = (a/b)
// },
// multiplyClick: function(a,b) {
//     this.number = (a*b)
// }