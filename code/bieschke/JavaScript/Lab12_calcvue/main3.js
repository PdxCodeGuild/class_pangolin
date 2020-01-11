Vue.component('clear', {
    template: `<div v-on:click.prevent="$emit('clear')" class="btn">C</div>`
})

Vue.component('sign', {
    template: `<div v-on:click.prevent="$emit('sign')" class="btn">+/-</div>`
})

Vue.component('pct', {
    template: `<div v-on:click.prevent="$emit('pct')" class="btn">%</div>`
})

Vue.component('pct', {
    template: `<div v-on:click.prevent="$emit('pct')" class="btn">%</div>`
})

Vue.component('add', {
    template: `<div v-on:click.prevent="$emit('add')" class="btn">+</div>`
})

Vue.component('subtract', {
    template: `<div v-on:click.prevent="$emit('sub')" class="btn">-</div>`
})

Vue.component('mult', {
    template: `<div v-on:click.prevent="$emit('mult')" class="btn">*</div>`
})

Vue.component('division', {
    template: `<div v-on:click.prevent="$emit('division')" class="btn">/</div>`
})

Vue.component('equal', {
    template: `<div v-on:click.prevent="$emit('equal')" class="btn">=</div>`
})

Vue.component('dot', {
    template: `<div v-on:click.prevent="$emit('dot')" class="btn">.</div>`
})

Vue.component('digit', {
    props: ['digit'],
    template: `<div v-on:click.prevent="$emit('digit', digit)">{{digit}}</div>`
})

let vm = new Vue({
    el: '#app', //element
    data: {
        current: '',
        previous: '',
        operator: null,
    },

    methods: {
        addToDisplay: function(digit) {
            this.current += digit;
        },

        clear: function () {
            this.current = '';
        },

        sign: function () {
            this.current = this.current.charAt(0) === '-' ?
                this.current.slice(1) : `-${this.current}`;
        },
        pct: function () {
            this.current = `${parseFloat(this.current) / 100}`
        },
        append: function (number) {
            if (this.operatorClicked) {
                this.current = '';
                this.operatorClicked = false;
            }
            this.current = `${this.current}${number}`
        },
        dot: function () {
            if (this.current.indexOf('.') === -1) {
                this.append('.');
            }
        },
        setPrevious: function () {
            this.previous = this.current;
            this.operatorClicked = true;
            this.current = '';
        },
        divide: function () {
            this.operator = (a, b) => a / b;
            this.setPrevious()
        },
        mult: function () {
            this.operator = (a, b) => a * b;
            this.setPrevious()
        },
        subtract: function () {
            this.operator = (a, b) => a - b;
            this.setPrevious()
        },
        add: function () {
            this.operator = (a, b) => a + b;
            this.setPrevious()
        },
        equal: function () {
            rep = parseFloat(this.current);
            this.current = `${this.operator(
                parseFloat(this.previous),
                parseFloat(this.current)
            )}`;

            this.setPrevious = null;
            result = `${this.operator(this.current, rep)}`
            this.current = result;
        }
    }
});