let vm = new Vue({
    // element (el) selected by id (#)
    el: '#app',
    // data within element
    data: {
        todos: [],
        // adds binding element
        newTodoItem: {
            id: 1,
            text: "",
            completed: false,
            color: "#000000"
        }
    },
    // methods empoyed 
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
       deleteTodo: function(todoItem, e) {
        this.todos.splice(this.todos.indexOf(todoItem), 1);
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
        console.log("It loaded!");
    }
});