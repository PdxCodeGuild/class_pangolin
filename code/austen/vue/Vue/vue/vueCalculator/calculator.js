Vue.component('numbers', {
    props: ['num'],
    template: `
    <button v-on:click="$emit('digit',num)">{{num}}</button>
    `
});



let vm = new Vue({
    el:"#app",
    data: function() {
        return {
        current: "",
        previous: null,
        // sub:[],
        operation: null,
        operatorClick: false,
        }
    },
    methods:{
       numClick: function(digit){
           if (this.operatorClick){
               this.current = '';
               this.operatorClick = false;
           }
           this.current = `${this.current}${digit}`
           console.log(digit)
           return (this.current)
       },
       clrClick:function(){
            this.current = '';
       },
       oprClick:function(){
            this.current = this.current.charAt(0) ==='-' ?
                this.current.slice(1) : `-${this.current}`;
       },
       percentClick:function(){
            this.current = `${parseFloat(this.current)/100}`;
       },
       dotClick:function(){
            if (this.current.indexOf('0.')===-1){
                this.numClick('.');
            }
       },
       addClick: function(){
            this.operation = (a,b) => a+b;
            this.operatorClick = true;
            this.previous = this.current;
    
        },
        minusClick: function(){
            this.operation = (a,b) => b-a;
            this.operatorClick = true;
            this.previous = this.current;
        },
        timesClick: function(){
            this.operation = (a,b) => a*b;
            this.operatorClick = true;
            this.previous = this.current;
        },
        divideClick: function(){
            this.operation = (a,b) => a/b;
            this.operatorClick = true;
            this.previous = this.current;
        },
        eqlClick: function(){
            this.current = `${this.operation(
                parseFloat(this.current),
                parseFloat(this.previous)
                )}`;
                this.previous = null;
        },
        backspaceClick: function(){
            this.current = this.current.pop()
            return (this.current)
        }
    }
       
})