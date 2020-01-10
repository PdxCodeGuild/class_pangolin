let vm = new Vue({
    el: '#app',
    data: {
        userInput: "",
        result: [],
        name: ""
    },
    methods: {
        getRandomPerson: function() {
            axios({
                method: 'get',
                url: 'https://randomuser.me/api/',
                dataType: 'json',
                params: {
                    filter: this.name.first
                },
            }).then(response => this.result = response.data.results);
        }
    }
});