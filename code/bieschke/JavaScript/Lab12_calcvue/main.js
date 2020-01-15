let vm = new Vue({
    el: '#app', //element
    data: {
        current: '',
        previous: '',
        operator: null,
    },
    methods: {
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
        },
        divide: function () {
            this.operator = (a, b) => a / b;
            this.setPrevious()
        },
        mult: function () {
            this.operator = (a, b) => a * b;
            this.setPrevious()
        },
        sub: function () {
            this.operator = (a, b) => a - b;
            this.setPrevious()
        },
        add: function () {
            this.operator = (a, b) => a + b;
            this.setPrevious()
        },
        equal: function () {
            this.current = `${this.operator(
                parseFloat(this.previous),
                parseFloat(this.current)

            )}`;
            this.previous = null;

        }
    }
});