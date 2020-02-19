let vm = new Vue({
    el: '#app',
    data: {
        userInput: "",
        result: [],
        name: "",
        search: "",
        store: [],
        filtered: []
    },
    methods: {
        getRandomPerson: function() {
            axios({
                method: 'get',
                url: 'https://randomuser.me/api/',
                dataType: 'json',
            }).then(response => this.result = response.data.results);
        },
    }
});