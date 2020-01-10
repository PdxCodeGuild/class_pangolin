let vm = new Vue({
  el: '#app',
  data: {
      current: '123',
      previous: '',
      operator: '',
    },

  methods: {
    append(number) {
      this.current = `${this.current}${number}`;
      console.log(number)
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
      this.current = this.current + this.previous
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

Vue.component('digit', ({
  prop: ['digit'],
  template: `<div class="button" @click="$emit(append('digit'))"></div>`
})),

Vue.component('equals', ({
  template: '<div class="button" v-on:click="equals()"></div>'
})),

Vue.component('multiply', ({
  template: '<div class="button" v-on:click="assignOperator('*')"></div>'
})),

Vue.component('add', ({
  template: `<div class="button" v-on:click.prevent="$emit('assignOperator('+')')"></div>`
})),

Vue.component('subtract', ({
  template: `<div class="button" v-on:click.prevent="$emit('assignOperator('-')')"></div>`
})),

Vue.component('divide', ({
  template: `<div class="button" v-on:click.prevent="$emit('assignOperator('/')')"></div>`
})),

Vue.component('percent', ({
  template: `<div class="button" v-on:click.prevent="$emit('assignOperator('%')')"></div>`
})),

Vue.component('sign', ({
  template: `<div class="button" v-on:click.prevent="$emit('assignOperator('+/-')')"></div>`
})),

Vue.component('clear', ({
  template: `<div class="button" v-on:click.prevent="$emit('clear')"></div>`
})),

Vue.component('display', ({
  template: `<div class="display"></div>`
}))
