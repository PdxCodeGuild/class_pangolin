// + button component
vue.component('add', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// - button component
vue.component('subtract', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// * button component
vue.component('multiply', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// / button component
vue.component('divide', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// = button component
vue.component('equals', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// clear button component
vue.component('clear', {
    data: function() {
        return {
            //
        }
    },
    template: `
        <form>
            <button></button>
        </form>
    `,
    methods: {
        //
    }
});

// num buttons component
Vue.component('num-button', {
    props: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'],
    template: `
        <form
            <button></button>
        </form>
    `,
});

let vm = new Vue({
    // element (el) selected by id (#)
    el: '#app',
    // data within element
    data: {
        current_total: [],
        current_subtotal: [],
        active_key: []
    },
    // methods empoyed 
    methods: {
       //: function() {
           this.//.push(//);
        } 
    },
    computed: //: function() {
        return this.//.filter(item => item.//);
    },
    mounted: function() {
        console.log("It loaded!");
    }
});