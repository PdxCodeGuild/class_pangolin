let vm = new Vue({
    el: "#app",
    data: {
        message: "Hello World!",
        visible: true,
        todos: [
            {text: 'Learn JS', id: 0},
            {text: 'Learn Vue', id: 1},
            {text: 'Build something', id: 2},
        ],
        groceries: [
            {id: 0, food: "apple"},
            {id: 1, food: "banana"},
            {id: 2, food: "orange"}
        ],
    },
    methods: {
        reverseFunction: function(e){
            this.message = this.message.split('').reverse().join('');
        },
        deleteTodo: function(todo){
            console.log(todo.text);
            for (let t of this.todos){
                if (t.id === todo.id){
                    delete t;
                }
            }
        }
    },
});