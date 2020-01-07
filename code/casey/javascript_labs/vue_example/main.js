Vue.component('add-item', {
    data: function() {
        return {
            id: 1,
            text: "",
            completed: false,
            color: "#000000"
        }
    },
    template: `
        <form>
            <input type="text" placeholder="New grocery item" v-model="text"/>
            <input type="color" v-model="color"/>
            <button v-on:click.prevent="add">Add</button>
        </form>
    `,
    methods: {
        add: function() {
            this.$emit('add', {id: this.id, text: this.text, completed: this.completed, color: this.color})
            this.id++
        }
    }
});

Vue.component('grocery-item', {
    props: ['grocery'],
    template: `
        <li>
            <p v-bind:class="{completed: grocery.completed}" v-bind:style="{color: grocery.color}">{{ grocery.text }}</p>
            <input type="checkbox" v-model="grocery.completed"/>
            <input type="color" v-model="grocery.color"/>
            <button v-on:click=$emit('delete-grocery', grocery)">Delete</button>
        </li>
    `,
});

let vm = new Vue({
    // element (el) selected by id (#)
    el: '#app',
    // data within element
    data: {
        groceries: [],
    },
    // methods empoyed 
    methods: {
       addGrocery: function(newGroceryItem) {
           this.groceries.push(newGroceryItem);
        }, 
       deleteGrocery: function(groceryItem) {
           this.groceries.splice(this.groceries.indexOf(groceryItem), 1);
        }
    },
    computed: {
        completedItems: function() {
            return this.groceries.filter(item => item.completed);
        },
        incompletedItems: function() {
            return this.groceries.filter(item => !item.completed);
        }
    },
    mounted: function() {
        console.log("It loaded!");
    }
});