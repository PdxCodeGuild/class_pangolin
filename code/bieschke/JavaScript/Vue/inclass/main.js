let vm = new Vue({
    el: '#app', //element
    data: {     //model to store the state of the webpage
        message: 'Hello World!', //div message in html doc
        visible: true,
        todos: [
            { text: 'get' },
            { text: 'after' },
            { text: 'it' },
        ]
    },
    methods: {
        redButton: function() {
            this.message = this.message.split('').reverse().join('')    //how to reverse things in JS. gross
        }
    }
});