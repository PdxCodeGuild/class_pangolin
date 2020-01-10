let vm = new Vue({
    el: '#app',
    data: {
        userInput: "",
        result: []
    },
    methods: {
        getQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    Authorization: 'Token token="898ce244ffea7807a375ce02f5a27f99"'
                },
                params: {
                    filter: this.userInput
                },
            }).then(response => this.result = response.data.quotes);
        }
    }
});