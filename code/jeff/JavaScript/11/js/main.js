let vm = new Vue({
    el: '#app',
    data: {
        todos: [],
        newTodoItem: {
            id: 1,
            text: "",
            completed: false,
            color: "#000000"
        }
    },
    methods: {
        addTodo: function() {
            this.todos.push({
                id: this.newTodoItem.id,
                text: this.newTodoItem.text,
                completed: this.newTodoItem.completed,
                color: this.newTodoItem.color
            });
            this.newTodoItem.id++;
        },
        deleteTodo: function(TodoItem, e) {
            this.todos.splice(this.todos.indexOf(todoItem), 1)
        }
    },
    computed: {
        completedItems: function() {
            return this.todos.filter(item => item.completed);
        },
        incompletedItems: function() {
            return this.todos.filter(item => !item.completed);
        }
    },
    mounted: function() {
        console.log("It loaded");
    }
});