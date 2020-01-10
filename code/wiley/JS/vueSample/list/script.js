Vue.component('grocery-item', {
    props: ['grocery'], // Use props over data if you are getting the information from outside the function. 
    template: `
        <li>
        <p v-bind:class="{completed: grocery.completed}" v-bind:style="{color: grocery.color}">{{ grocery.text }}</p>
        <input type="checkbox" v-model="grocery.completed"/>
        <input type="color" v-model="grocery.color"/>
        <button v-on:click="$emit('delete-grocery',grocery )">Delete</button>
        </li>
    `, //templates are html injections, or blue-prints to cleanly generating your HTML formats
    methods: {
        // deleteGrocery: function(groceryItem, e){
        //     this.groceries.splice(this.groceries.indexOf(groceryItem),1)
        // }  
        //<button v-on:click="deleteGrocery(grocery,$event)">Delete</button>
    }
});


let vm = new Vue({
    el: "#app",
    data: {
        groceries: [],
        newGroceryItem: {
            id: 1,
            text: "",
            completed: false,
            color: "#0F4C81",
        }
    },
    methods: {
        addGrocery: function() {
            this.groceries.push({
                id: this.newGroceryItem.id,
                text: this.newGroceryItem.text,
                completed: this.newGroceryItem.completed,
                color: this.newGroceryItem.color,
            });
            this.newGroceryItem.id++; //new id for each new item
            },
        deleteGrocery: function(groceryItem, groceryIndex, e){
            this.groceries.splice(this.groceries.indexOf(groceryItem),1)
        }
    },
    computed: {
        completedItems: function() {
            return this.groceries.filter(item => item.completed)
        },
        incompletedItems: function() {
            return this.groceries.filter(item => !item.completed)
        }
    },
    mounted: function() {
        console.log("Get Loaded")
        // this.groceries = JSON.parse(localStorage.getItem("groceries"));
        // window.addEventListener("beforeunload", function() {
        //     localStorage.setItem('groceries', JSON.stringify(this.groceries))
        
    }
}
);