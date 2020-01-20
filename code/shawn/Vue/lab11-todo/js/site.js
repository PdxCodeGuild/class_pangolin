

let app = new Vue({
    el: "#app",
    data: {
        items: [],
        newItem: {
            id: 1, 
            text: "",
            completed: false,
        },
    },
    methods: {
        addItem: function(){
            this.items.push( {
                id: this.newItem.id, 
                text: this.newItem.text,
                completed: this.newItem.completed,
            })
            this.newItem.id++;
        },
        deleteItem: function(item){
            this.items.splice(this.items.indexOf(item), 1);
        },
        clearItems: function(){
            this.items = [];
        }
    },
    computed: {
        completedItems: function(){
            return this.items.filter(item => item.completed);
        },
        incompleteItems: function(){
            return this.items.filter(item => !item.completed);
        }
    },
    mounted: function(){    //mounted automatically happens once everything is on the page
        // this.items = JSON.parse(localStorage.getItem("items"));
        // window.addEventListener("beforeunload", function(){
        //     localStorage.setItem('items', JSON.stringify(this.items));
        // });
        console.log("loaded the page.")
    }
});