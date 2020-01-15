let vm = new Vue({
    el: '#app',
    data: {
        groceries: [],
        newGroceryItem: {
            id: 1,
            text: "",
            completed: false,
            color: "#000000",
        }
    },
    methods: {
        addGrocery: function() {
            this.groceries.push({
                id: this.newGroceryItem.id,
                text: this.newGroceryItem.text,
                completed: this.newGroceryItem.completed,
                color: this.newGroceryItem.color
            });
            this.newGroceryItem.id++;
        },
        deleteGrocery: function(groceryItem, groceryIndex, e) {
            this.groceries.splice(groceryIndex,1);
        }
    },
    computed: {
        completedItems: function() {
            return this.groceries.filter(item => item.completed);
        },
        incompleteItems: function() {
            return this.groceries.filter(item => !item.completed)
        }
    }
});