Vue.component('calc-item', {
    mounted: function() {
        this.clear()
    },
    props: { answer: '', logList: '', current: '' },
    template: `
        <div class="calculator">
        <div class="answer">{{ answer }}</div>
        <div class="display">{{ logList + current }}</div>
        <div v-on:click="clear" id="clear" class="btn operator">C</div>
        <div v-on:click="sign" id="sign" class="btn operator">+/-</div>
        <div v-on:click="percent" id="percent" class="btn operator">
            %
        </div>
        <div v-on:click="divide" id="divide" class="btn operator">
            /
        </div>
        <div v-on:click="append('7')" id="n7" class="btn">7</div>
        <div v-on:click="append('8')" id="n8" class="btn">8</div>
        <div v-on:click="append('9')" id="n9" class="btn">9</div>
        <div v-on:click="times" id="times" class="btn operator">*</div>
        <div v-on:click="append('4')" id="n4" class="btn">4</div>
        <div v-on:click="append('5')" id="n5" class="btn">5</div>
        <div v-on:click="append('6')" id="n6" class="btn">6</div>
        <div v-on:click="minus" id="minus" class="btn operator">-</div>
        <div v-on:click="append('1')" id="n1" class="btn">1</div>
        <div v-on:click="append('2')" id="n2" class="btn">2</div>
        <div v-on:click="append('3')" id="n3" class="btn">3</div>
        <div v-on:click="plus" id="plus" class="btn operator">+</div>
        <div v-on:click="append('0')" id="n0" class="zero">0</div>
        <div v-on:click="dot" id="dot" class="btn">.</div>
        <div v-on:click="equal" id="equal" class="btn operator">=</div>
        </div>
    `,
    methods: {
        append(number) {
            if (this.operatorClicked) {
                this.current = "";
                this.operatorClicked = false;
            }
            this.animateNumber(`n${number}`);
            this.current = `${this.current}${number}`;
        },
        addtoLog(operator) {
            if (this.operatorClicked == false) {
                this.logList += `${this.current} ${operator} `;
                this.current = "";
                this.operatorClicked = true;
            }
        },
        animateNumber(number) {

        },
        animateOperator(operator) {

        },
        clear() {
            this.animateOperator("clear");
            this.current = "";
            this.answer = "";
            this.logList = "";
            this.operatorClicked = false;
        },
        sign() {
            this.animateOperator("sign");
            if (this.current != "") {
                this.current =
                    this.current.charAt(0) === "-" ?
                    this.current.slice(1) :
                    `-${this.current}`;
            }
        },
        percent() {
            this.animateOperator("percent");
            if (this.current != "") {
                this.current = `${parseFloat(this.current) / 100}`;
            }
        },
        dot() {
            this.animateNumber("dot");
            if (this.current.indexOf(".") === -1) {
                this.append(".");
            }
        },
        divide() {
            this.animateOperator("divide");
            this.addtoLog("/");
        },
        times() {
            this.animateOperator("times");
            this.addtoLog("*");
        },
        minus() {
            this.animateOperator("minus");
            this.addtoLog("-");
        },
        plus() {
            this.animateOperator("plus");
            this.addtoLog("+");
        },
        equal() {
            this.animateOperator("equal");
            if (this.operatorClicked == false) {
                this.answer = eval(this.logList + this.current);
            } else {
                this.answer = "error";
            }
        },
    },
})

new Vue({
    el: "#app",
    data() {
        return {
            logList: "",
            current: "",
            answer: "",
            operatorClicked: true
        };
    },
});