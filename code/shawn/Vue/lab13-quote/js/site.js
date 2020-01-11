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
            <h3 class="author-text"><a :href="wikiLink">{{quoteAuthor}}</a></h3>
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
    }, 
    computed: {
        wikiLink: function(){
            return 'https://en.wikipedia.org/wiki/' + this.quoteAuthor.replace(" ", "_")
        }
    }
});

Vue.component('quote-list', {
    props: ['quotes', 'pagenum'],
    template: `
        <ul>
            <h3 v-if="quotes.length > 0">Page: {{pagenum}}</h3>
            <li v-for="quote in quotes">
                <h4 class="quote-text">{{quote.body}}</h4>
                <h5 class="author-text">{{quote.author}}</h5>
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
            return
        }
    }
});