Vue.component('clear', {
    data: function() {
        console.log()
        return {
            value: 0,
            logs: []
        }
    },

    template: `
        <div class="calculator-col">
            <button class="calculator-btn gray actions" 
            v-on:click="clear()">C</button>
        </div>
    `,
    methods: {
        clear: function() {
            console.log('clear')
            this.$emit('c', {
                value: this.value,
                logs: this.logs
            })
        }
    }
})

Vue.component('delete', {
    data: function() {
        console.log()
        return {
            value: 0,
            logs: []
        }
    },

    template: `
  <div class = 'calculator-col'>
    <button class = 'calculator-btn gray action' 
    v-on:click = 'del()'>del</button> 
  </div>
  `,
    methods: {
        del: function() {
            console.log('del')
            this.$emit('del', {
                value: this.value,
                logs: this.logs
            })
        }
    }
})

Vue.component('equals', {
    data: function() {
        console.log()
        return {
            value: 0,
            logs: []
        }
    },

    template: `
    <div class='calculator-col'>
      <button class='calculator-btn accent action' v-on:click='getResult()'>=</button>
    </div>
  `,
    methods: {
        getResult: function() {
            console.log('getResult')
            this.$emit('equals', {
                value: this.value,
                logs: this.logs
            })
        }
    }
})

Vue.component('number-btn', {
    props: ['num'],
    template: `
    <div class='calculator-col'>
      <button class='calculator-btn' v-on:click="$emit('add', num)">{{ num }}</button>
    </div>
  `,
})

Vue.component('symbol-btn', {
    props: ['symbol'],
    template: `
  <div class='calculator-col'>
    <button class='calculator-btn accent action' v-on:click='$emit("add", symbol)'>{{ symbol }}</button>
  </div>
  `,
})

Vue.component('zero-btn', {
    props: ['num'],
    template: `
  <div class='calculator-col wide'>
    <button class='calculator-btn' v-on:click='$emit("add", num)'>{{ num }}</button>
  </div>
  `,
})

let vm = new Vue({
    el: '#calculator',
    data: {
        value: 0,
        logs: []
    },
    methods: {
        addExpression(e) {
            if (Number.isInteger(this.value))
                this.value = '';
            this.value += e;
        },
        getResult() {
            let log = this.value;
            this.value = eval(this.value);
            this.logs.push(log + `=${this.value}`);
        },
        clear() {
            this.value = 0;
        },
        del() {
            this.value = this.value.slice(0, -1);
        }
    }
})