
Vue.component('todo-item', {
    template:'\
    <li>\
        {{ title }}\
        <button v-on:click="$emit(\'remove\')">Remove</button>\
        <input type="checkbox" :completed="false"/>\
    </li>\
    ',
    props: ['title', 'completed']
})

let vm= new Vue({
    el: '#todo-list-example',
    data: {
        newTodoText: '',
        todos: [],
        nextTodoId: 1,
        completed: false,
    },
    methods: {
        addNewTodo: function() {
            this.todos.push({
                id: this.nextTodoId++,
                title: this.newTodoText,
                completed: this.newTodocompleted
            })
            this.newTodoText = ''
        }
    },
    computed: {
        completedItems: function() {
            return this.todos.filter(item =>item.completed);
        },
        incompletedItems: function() {
            return this.todos.filter(item =>!item.completed);
        }
    }
})