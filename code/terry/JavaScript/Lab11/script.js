let vm = new Vue({
    el: '#app',
    data: {
        toDo: [],
        newToDoItem: {
            id: 1,
            text: "",
            completed: false,
            color: "#0F4C81",
        }
    },
    methods: {
        addToDo: function() {
            this.toDo.push({
                id: this.newToDoItem.id,
                text: this.newToDoItem.text,
                completed: this.newToDoItem.completed,
            });
            this.newToDoItem.id++;
        },
        deleteGrocery: function(toDoItem, e) {
            this.toDo.splice(this.toDo.indexOf(toDoItem), 1);
        }
    },
    computed: {
        completedItems: function() {
            return this.toDo.filter(item => item.completed);
        },
        incompletedItems: function() {
            return this.toDo.filter(item => !item.completed);
        }
    },
    mounted: function() {
        console.log('Loaded');
    }
});