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
        this.$emit('getQuote', {id:this.id, text:this.text}),
        this.id++
    },
});

// get the info from the api 
let vm = new Vue ({
    el: '#app',
    data: {
        quoteInput: "",
        inputType: "",
        results: [],
        // results2: [],
    },
    methods: {
        getQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                headers: {
                    Authorization: 'Token token="50f3400c99d67bd71bea7d473c15ce73"'
                },

                // render the info into the HTML page so it can be seen on webpage
            }).then(res => this.results = res.data.quotes);
            // }).then(res => console.log(res));
        },
    

    // get the info from the api
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

                // render the info into the HTML page so it can be seen on webpage
            }).then((res) => {
                let answers = res.data.quotes;
                // this.results = answers
                console.log(answers)
                let filterquote = answers[Math.floor(Math.random() * answers.length)];
                this.results = answers
                console.log(filterquote)

                // console.log(option)
                // log the errors in the console.log so that you can see what went wrong
            })
        }
    },
    mounted:function() {
        this.getQuote()
    }
})
