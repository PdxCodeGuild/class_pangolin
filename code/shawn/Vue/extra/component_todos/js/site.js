Vue.component('todo-item', {
    props: ['todo'],
    template: `<li> 
                    {{ todo.text }}
                    <button v-if="todo.isComplete === false" v-on:click="todo.isComplete = true">✓</button>
                    <button v-on:click="removeItem">x</button>
                </li>`,
    methods: {
        removeItem: function(){
            console.log("trying to remove item");
            
        }
    }
});


let app = new Vue({
    el: "#app",
    data: {
        activeTodoList: [
            { id: 0, text: "go to store", isComplete: false},
            { id: 1, text: "get shopping cart", isComplete: false},
            { id: 2, text: "shop", isComplete: false},
        ], 
        completedTodoList: [
            { id: 0, text: "wake up", isComplete: true},
            { id: 1, text: "shower", isComplete: true},
            { id: 2, text: "get dressed", isComplete: true},
        ], 
    }
});