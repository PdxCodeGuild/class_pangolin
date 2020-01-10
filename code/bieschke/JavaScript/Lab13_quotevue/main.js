Vue.component('get-quote', {
    template: `<div v-on:click.prevent="$emit('get-quote')" class='btn'>QOTD</div>`
})

Vue.component('funny-button', {
    template: `<div v-on:click.prevent="$emit('funny-button')" class='btn'>Funny</div>`
})

Vue.component('search-button', {
    template: `<div v-on:click.prevent="$emit('search-button')" class='btn'>Find one</div>`
})

Vue.component('search-button2', {
    template: `<div v-on:click.prevent="$emit('search-button2')" class='btn'>Find all</div>`
})

Vue.component('clear', {
    template: `<div v-on:click.prevent="$emit('clear')" class='btn'>Clear Results</div>`
})

let vm = new Vue({
    el: '#app',
    data: {
        quote: {
            body: null,
            author: null,
        },
        database: [],
    },

    methods: {
        //gives a random quote
        getQuote: function () {
            axios({
                method: "GET",
                url: 'https://favqs.com/api/qotd',
                headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
            }).then(response => {
                this.database = response.data.quote;
                this.quote.body = response.data.quote.body,
                    this.quote.author = response.data.quote.author
            }).catch(error => console.log(error))
        },
        //searches the database for quotes containing the string 'funny', and returns a random one
        funnyButton: function () {
            axios({
                method: "GET",
                url: 'https://favqs.com/api/quotes/?filter=funny',
                headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
            }).then(response => {
                this.database = response.data.quotes;
                let funny = Math.floor(Math.random() * response.data.quotes.length);
                this.quote.body = response.data.quotes[funny].body,
                    this.quote.author = response.data.quotes[funny].author
            }).catch(error => console.log(error))
        },
        //provides a single quote based on user input
        searchButton: function () {
            let searchTerm = document.getElementById("input").value;
            axios({
                method: "GET",
                url: 'https://favqs.com/api/quotes/?filter=' + searchTerm,
                headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
            }).then(response => {
                this.database = response.data.quotes;
                let usr = Math.floor(Math.random() * response.data.quotes.length);
                this.quote.body = response.data.quotes[usr].body,
                    this.quote.author = response.data.quotes[usr].author
            }).catch(error => console.log(error))
        },
        //provides a list of quotes containing user input
        searchButton2: function () {
            let searchTerm2 = document.getElementById("input2").value;
            axios({
                method: "GET",
                url: 'https://favqs.com/api/quotes/?filter=' + searchTerm2,
                headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
            }).then(response => {
                this.database = response.data.quotes;
                console.log(this.database)
                // Array.from().forEach(i => {
                //     this.quote.body = response.data.quotes[i].body,
                //     this.quote.author = response.data.quotes[i].author
            }).catch(error => console.log(error))
        },
        //clears all displayed quotes
        clear: function () {
                this.database = []
            }
        }
});

