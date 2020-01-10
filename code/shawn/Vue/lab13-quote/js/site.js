Vue.component('random-quote', {
    data: function () {
        return {
            quoteAuthor: '',
            quoteText: '',
            authorPic: '',
        }
    },
    template: `
        <div id="headline-quote">
            <h1 class="quote-text">{{quoteText}}</h1>
            <h3 class="author-text">{{quoteAuthor}}</h3>
            <img :src="authorPic">
            <button @click="getQuote">New quote</button>
        </div>
    `,
    methods: {

        getQuote: function () {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd",
                params: {}
            }).then(res => {
                this.quoteAuthor = res.data.quote.author;
                this.quoteText = res.data.quote.body;
                this.getPicture();
            });
        },

        getPicture: function () {
            // code for pulling up image here

        }
    },
    mounted: function () {
        this.getQuote();
    }
});

Vue.component('quote-list', {
    props: ['quotes'],
    template: `
        <ul>
            <li v-for="quote in quotes">
                <h6>{{quote.body}}</h6>
                <h5>{{quote.author}}</h5>
            </li>
        </ul>
    `,
    methods: {
    }
});

let vm = new Vue({
    el: "#app",
    data: {
        searchTerms: '',
        quoteList: [],
        pages: [],
        pageNumber: 1,
    },
    methods: {
        newQuotes: function(){
            this.pages = []
            this.pageNumber = 1;
            this.updateList();
        },
        getQuotes: function () {
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                params: {
                    filter: this.searchTerms,
                    page: this.pageNumber,
                },
                headers: {
                    'Authorization': `Token token=${apikey}`    // from secrets.js
                }
            }).then(res => {
                console.log("quotes found, adding to pages array");
                this.pages.push(res.data.quotes);
                console.log("pages:")
                console.log(this.pages)
                this.quoteList = this.pages[this.pageNumber - 1];
            });

        },
        prevPage: function () {
            this.pageNumber--;
            this.updateList();
        },
        nextPage: function () {
            this.pageNumber++;
            this.updateList();
        },
        updateList: function () {
            console.log(`pages.length is ${this.pages.length}`)
            if (this.pageNumber > this.pages.length ) {
                console.log("getting new quotes")
                this.getQuotes(this.pageNumber);
            } 
            this.quoteList = this.pages[this.pageNumber - 1];
        }

    },
    mounted: function () {

    },
    computed: {
        nextQuote: function(){
        
        }
    }
});