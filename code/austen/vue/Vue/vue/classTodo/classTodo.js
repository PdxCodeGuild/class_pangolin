Vue.component('add-item', {
    data: function() {
        return {
        id: 1,
        text:'',
        completed: false,
        color: ''
        }
    },
    template: `
        <form>
            <input type="text" placeholder="New grocery Item" v-model="text"/>
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
            <p 
                v-bind:class="{completed: grocery.completed}"
                v-bind:style="{color: grocery.color}"
            >
                {{ grocery.text }}
            </p>
            <input type="checkbox" v-model="grocery.completed"/>
            <input type="color" v-model="grocery.color"/>
            <button v-on:click="$emit('delete-grocery', grocery)">Delete</button>
        </li>
    `,
    methods: {
        // <button v-on:click="deleteGrocery(grocery, $event)">Delete</button>
    //     deleteGrocery: function(groceryItem, e){
    //         // this.groceries.splice(groceryIndex,1);
    //         this.$parent.groceries.splice(this.$parent.groceries.indexOf(groceryItem),1);
    //     }
    //^^^this this.$parent is not as effective just use $emit and use the delete function below.
    }
});

let vm = new Vue ({
    el:"#app",
    data: {
        groceries: [],
    },
    methods: {
        addGrocery: function(newGroceryItem) {
            this.groceries.push(newGroceryItem);
        },
        deleteGrocery: function(groceryItem) {
            // this.groceries.splice(groceryIndex,1);
            this.groceries.splice(this.groceries.indexOf(groceryItem),1);
        }
    },
    computed: {
        completedItems: function() {
            return this.groceries.filter(item =>item.completed);
        },
        incompletedItems: function() {
            return this.groceries.filter(item => !item.completed);
        }
    },
    mounted: function() {
       console.log("It loaded!");
    }
});