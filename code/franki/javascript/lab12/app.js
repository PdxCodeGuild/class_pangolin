Vue.component('digit', ({
  props: ['number'],
  template: `<div @click.prevent="$emit('digit', number)">{{ number }}</div>`
}));

Vue.component('equals', ({
  template: `<div @click.prevent="$emit('equals')">=</div>`
}));

Vue.component('operation', ({
  props: ['operator'],
  template: `<div class="button" @click.prevent="$emit('operation', operator)">{{ operator }}</div>`
}));

Vue.component('percent', ({
  template: `<div class="button" @click="$emit('percent')">%</div>`
}));

Vue.component('sign', ({
  template: `<div class="button" @click="$emit('invert-sign')">+/-</div>`
}));

Vue.component('clear', ({
  template: `<div class="button" @click="$emit('clear')">C</div>`
}));

Vue.component('display', ({
  props: ['displayValue'], 
  template: `<div class="display">{{ displayValue }}</div>`
}));

let vm = new Vue({
  el: '#app',
  data: {
      current: '',
      previous: '',
      operator: '',
    },

  methods: {
    appendToDisplay: function(number) {
      this.current = this.current + number
    },

    clear() {
      this.current = "";
      this.previous = "";
    },

    percent() {
      this.current = `${parseFloat(this.current) / 100}`;
    },
    
    sign() {
      this.current = this.current.charAt(0) === '-' ?
      this.current.slice(1) : `-${this.current}`;
    },
      
    add() {
      this.current = parseFloat(this.previous) + parseFloat(this.current)
    },

    subtract() {
      this.current = this.current - this.previous
    },

    multiply() {
      this.current = this.current * this.previous
    },

    divide() {
      this.current = this.previous / this.current
    },

    assignOperator(operator) {
      this.operator = operator,
      this.previous = this.current,
      this.current = ""
    },

    equals() {
      if (this.operator === '-') {
        this.subtract();
      } else if (this.operator === '+') {
        this.add();
      } else if (this.operator === 'x') {
        this.multiply();
      } else if (this.operator === '%') {
        this.percent()
      } else if (this.operator === '+/-') {
        this.sign()
      } else if (this.operator === '/') {
        this.divide()
      }
    }
  }
});


