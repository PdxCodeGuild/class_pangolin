Vue.component('numbers', {
    props: ['num'],
    template: `
    <button v-on:click="$emit('digit',num)">{{num}}</button>
    <input v-model:
    `
});



let vm = new Vue({
    el:"#app",
    data: function() {
        return {
        current: "",
        previous: null,
        operation: null,
        operatorClick: false,
        readout:""
        }
    },
    methods:{
        numClick: function(digit){
           if (this.operatorClick){
               this.current = '';
               this.operatorClick = false;
           }
           this.current = `${this.current}${digit}`
           this.readout +=`${digit}`
           console.log(digit)
        //    return (this.current)
       },
       clrClick:function(){
            this.current = '';
            this.readout = '';
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
            this.readout += "+"
        },
        minusClick: function(){
            this.operation = (a,b) => a-b;
            this.operatorClick = true;
            this.previous = this.current;
            this.readout += "-"
        },
        timesClick: function(){
            this.operation = (a,b) => a*b;
            this.operatorClick = true;
            this.previous = this.current;
            this.readout += "x"
        },
        divideClick: function(){
            this.operation = (a,b) => a/b;
            this.operatorClick = true;
            this.previous = this.current;
            this.readout += "%"
        },
        eqlClick: function(){
           
            this.current = `${this.operation(
                parseFloat(this.previous),
                parseFloat(this.current)
                )}`;
                let check= isNaN(this.current)
                console.log(check)
                if (this.current === "NaN"){
                    this.current = 0
                    return (this.current)
                }
                console.log(this.current)
                this.operatorClick = true;
            this.readout += "="
        },
        backspaceClick: function(){
            this.current = this.current.slice(0,-1)
            this.readout = this.readout.slice(0,-1)
            return (this.current)
        }
    },
    mounted: function() {
        window.addEventListener("keydown", function(event){
            if (event.defaultPrevented) {
                return;
            }
            if ("0123456789".includes(event.key)){
                vm.numClick(event.key)
                
            }
            if (event.key===("+")) {
                vm.addClick(event.key)
            }
            if (event.key===("-")) {
                vm.minusClick(event.key)
            }
            if (event.key===("*")) {
                vm.timesClick(event.key)
            }
            if (event.key===("/")) {
                vm.divideClick(event.key)
            }
            if (event.keyCode=== 13) {
                vm.eqlClick(event.key)
                return(this.current)
            }
            if (event.key===(".")) {
                vm.dotClick(event.key)
            }
            if (event.key===("c")) {
                vm.clrClick(event.key)
            }
            if (event.key=== "Backspace"){
                vm.backspaceClick(event.key)
            };
    })}
})