let vm = new Vue({
    el: '#app',
    data: {
        message: 'Hello World',
        visible: true,
        todos: [
            { text: 'Learn JavaScript'},
            { text: 'Learn Vue' },
            { text: 'Build something awesome'}
        ]
    },
    methods: {
        reverseMessage: function(e) {
            this.message = this.message.split('').reverse().join();
        }
    }

});
