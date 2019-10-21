let header = new Headers()
header.append('Authorization', 'Token token="4b3888849b4ef0bec9f217ffd39869a9"')

let app = new Vue({
  el: '#app',
  data: {
    quoteSearchInput: '',
    quotesLoaded: false,
    quotesError: false,
    quoteResults: [],
  },
  methods: {
    getQuotes: function() {
      fetch(`https://favqs.com/api/quotes?filter=${this.quoteSearchInput}`, {
        headers: header
      })
      .then(response => response.json())
      .then(response => (this.quoteResults = response))
      .then(response => (this.quotesLoaded = true))
      .catch(function(error) {
        console.log(error)
      });
    },
    addDogs: function(quote) {
      quote.body += ' DOGS DOGS DOGS';
    }
  }
});