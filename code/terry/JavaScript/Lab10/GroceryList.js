let vm = new Vue({
    el: '#app',
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
            });
            this.newGroceryItem.id++;
        },
        deleteGrocery: function(groceryItem, e) {
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
        console.log('Loaded');
    }
});