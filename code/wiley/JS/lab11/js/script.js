let vm = new Vue({
    el: "#app",
    data: {
        message: "test", //test message
        toDoList: [], //initializing Array to hold newToDos
        newToDo: {
            id:1, //initializing id values
            toDoText: "", //initializing text description
            completed: false, //initializing to completed === false
        },
    },
    methods: {
        addItem: function() { //function to add a newToDo to toDoList
            this.toDoList.push({
                id:this.newToDo.id,
                toDoText: this.newToDo.toDoText,
                completed: false,
            })
        console.log(this.newToDo)
        this.newToDo.id++; //increasing id# each new Item added
        },
        editItem: function() {
            //need to identify this toDo and append new text value
        },
        deleteItem: function() {
            
            }
            //need to identify the desired toDo via checkbox and then remove from the toDoList array. 
            
    },
    computed: {
        completedItems: function() {
            return this.toDoList.filter(item => item.completed)
        },
        incompletedItems: function() {
            return this.toDoList.filter(item => !item.completed)
        }
    },
    mounted: function() {
        console.log("loaded")
    }
});
