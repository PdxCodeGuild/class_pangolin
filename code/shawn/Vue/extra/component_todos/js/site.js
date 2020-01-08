Vue.component("add-item", {
    data: function(){
        return {
            id: 1,
            text: "",
            completed: false, 
        }
    },
    template: `
        <form>
            <input type="text" placeholder="New item" v-model="text" />
            <button v-on:click.prevent="add">Add</button>
            <button v-on:click.prevent="$emit('clear')">Clear All</button>
        </form>
        `,
    methods: {
        add: function(){
            this.$emit('add', {id: this.id, text: this.text, completed: this.completed});
            this.id++;
        }
    }
})

Vue.component('todo-item', {
    props: ['item'],    // this must be passed into the component
    template: `
        <li>
            <div class="buttons">
                <input type="checkbox" v-model="item.completed">
                <button v-on:click="$emit('delete-item', item)">Delete</button>
            </div>
            <p v-bind:class="{completed: item.completed}">{{ item.text }}</p>
        </li>`,
    // <button v-on:click="deleteItem(item)">Delete</button>
    methods: {
        // deleteItem: function (item) {
        //     this.$parent.items.splice(this.$parent.items.indexOf(item), 1);
        // },

    }

});

let app = new Vue({
    el: "#app",
    data: {
        items: []
    },
    methods: {
        addItem: function (e) {
            this.items.push(e);
        },
        deleteItem: function (item) {
            this.items.splice(this.items.indexOf(item), 1);
        },
        clearItems: function () {
            this.items = [];
        }
    },
    computed: {
        completedItems: function () {
            return this.items.filter(item => item.completed);
        },
        incompleteItems: function () {
            return this.items.filter(item => !item.completed);
        }
    },
    mounted: function () {    //mounted automatically happens once everything is on the page
        // this.items = JSON.parse(localStorage.getItem("items"));
        // window.addEventListener("beforeunload", function(){
        //     localStorage.setItem('items', JSON.stringify(this.items));
        // });
        console.log("loaded the page.")
    }
});
