var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    },
    methods: {
        reverseMessage: function() {
            this.message = this.message.split('').reverse().join('')
        }
    }
})
var app2 = new Vue({
    el:'#app-2',
    data: {
        message: 'You loaded this page on ' + new Date().toLocaleString()
    }
})
var app3 = new Vue({
    el: '#app-3',
    data: {
        todos: [
            {text: 'Learn JavaScript' },
            {text: 'Learn Vue' },
            {text: 'Build Something awsome' }
        ]
    }
})
var app4 = new Vue ({
    el: '#app-4',
    data:{
        message: 'Hello You'
    },
})

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
})
var app5 = new Vue ({
    el: '#app-5',
    data: {
        groceryList: [
            {id:0, text:'Veg'},
            {id:1, text:'Cheese'}
        ]
    }
})



let vm = new Vue({
    el: "#app",
    data: {
        routeInput: '',
        results: []
    },
    methods: {
        getBusses:function(){
            axios({
                get:"get",
                url:"the url goes here",
                params: {
                    appID: "the app id",
                    routes: this.routeInput
                }
            }),then(res => this.results = the parsed data that looks like data.something.something);
        }
    }
});