Vue.component('add-item', {
    data: function() {
        return {
            id: 1,
            text: "",
            completed: false,
            color: "#0F4C81",
        }

    },
    template: `
    <form>
        <input type="text" placeholder="new to do item" v-model="text">
        <input type="color" v-model="color">
        <button v-on:click.prevent="add">Add</button>
    </form>
    `,
    methods: {
        add: function() {
            this.$emit('add', { id: this.id, text: this.text, completed: this.completed, color: this.color })
            this.id++
        }
    }
})

Vue.component('todo-item', {
    props: ['todo'],
    template: `
    <li>
        <p v-bind:class="{completed: todo.completed}" v-bind:style="{color: todo.color}">
                    {{todo.text}}</p>
                <input type="checkbox" v-model="todo.completed">
                <input type="color" v-model="todo.color">
        <button v-on:click="$emit(deleteitem, todo)">Delete</button>
    </li>
    `,
    methods: {
        // deleteitem: function(todoitem, e) {
        //     this.$parent.todo.splice(this.todo.indexOf(todoitem), 1);
        // }
    }
});

let vm = new Vue({
    el: '#app',
    data: {
        todo: [],

    },
    methods: {
        addtodo: function(newtodoitem) {
            this.todo.push(newtodoitem);
        },
        deleteitem: function(todoitem, e) {
            this.todo.splice(this.todo.indexOf(todoitem), 1);
        }
    },
    computed: {
        completeditems: function() {
            return this.todo.filter(item => item.completed);
        },
        incompleteditems: function() {
            return this.todo.filter(item => !item.completed);
        }
    },
    mounted: function() {
        console.log('Loaded');
    }
});