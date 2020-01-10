let vm = new Vue ({
    el: '#app',
    data: {
        todo: [
        ],
        newToDoItem: {
            id: 1,
            text: "",
            completed: false,
            color:"",
        }
    },
    methods: {
        addToDo: function() {
            this.todo.push({           
                id: this.newToDoItem.id,
                text: this.newToDoItem.text,
                completed: this.newToDoItem.completed,
                color: this.newToDoItem.color
            });
            this.newToDoItem.id++;
        },
        deleteToDo: function(todoItem, todoIndex, e) {
            // this.todo.splice(todoIndex,1);
            this.todo.splice(this.todo.indexOf(todoItem),1);
        },  
    },
    computed: {
        completedItems: function() {
            return this.todo.filter(item => item.completed);
        },
        incompletedItems: function() {
            return this.todo.filter(item => !item.completed);
        }
    },
    mounted: function() {
        console.log("it loaded");
    }
});