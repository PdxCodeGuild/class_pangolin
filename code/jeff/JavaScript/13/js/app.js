let button = document.getElementById("quote-button");
let target = document.getElementById("target");
let option = document.getElementById("option");
let option_btn = document.getElementById("option-btn")
let option_result = document.getElementById("option-result")


Vue.component('random-quote', {
    props: ['quote'],
    data: function() {
        return {
            id: 1,
            text: "",
        }
    },
    template: `
        <div>
            <p>"{{quote.body}}"</p>
            <p><i><a v-bind:href="quote.url">"{{quote.author}}"</a></i></p>
        </div>
    `,
    getQuote: function() {
        this.$emit('getQuote', {
                id: this.id,
                text: this.text
            }),
            this.id++
    },
});

let vm = new Vue({
        el: '#app',
        data: {
            quoteInput: "",
            inputType: "",
            results: [],
        },
        methods: {
            getQuote: function() {
                axios({
                    method: "get",
                    url: "https://favqs.com/api/quotes",
                    headers: {
                        Authorization: 'Token token="50f3400c99d67bd71bea7d473c15ce73"',
                    },
                }).then(res => this.results = res.data.quotes);
            },

            getQuote1: function() {
                axios({
                    method: "get",
                    url: "https://favqs.com/api/quotes",

                    headers: {
                        Authorization: 'Token token="50f3400c99d67bd71bea7d473c15ce73"',
                    },
                    params: {
                        filter: this.quoteInput,
                        type: this.inputType,
                    }

                }).then((res) => {
                    let answers = res.data.quotes;
                    console.log(answers)
                    this.results = answers;
                })
            }
        },
        mounted: function() {
            this.getQuote()
        }
    })
    // * Let user enter search term & select whether to search by keyword, author, or tag.