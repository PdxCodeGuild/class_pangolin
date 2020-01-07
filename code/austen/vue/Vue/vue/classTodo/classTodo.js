let vm = new Vue ({
    el:"#app",
    data: {
        groceries: [],
        newGroceryItem: {
            id: 1,
            text:'',
            completed: false,
            color: ''
        }
    },
    methods: {
        addGrocery: function(){
            this.groceries.push({
                id: this.newGroceryItem.id,
                text: this.newGroceryItem.text,
                completed: this.newGroceryItem.completed,
                color: this.newGroceryItem.color
            });
            this.newGroceryItem.id++;
        },
        deleteGrocery: function(groceryItem, groceryIndex, e){
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