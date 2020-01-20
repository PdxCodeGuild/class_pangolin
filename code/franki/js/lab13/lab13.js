Vue.component('qdetail', {

  template: `
  <div>
  <ul v-if='quotesArray.length > 0'>
  <li v-for="quote in quotesArray" id="quotes">
        {{ quote.body }} {{ quote.author }}</li>
  </ul>
  </div>
  `
});

let vm = new Vue({
  el: '#app',
  data: {
      quotesArray: [],
      searchTerm: '',
    },
  methods: {
    searchQuotes: function() {
      this.searchTerm = document.getElementById("input").value;
      console.log(searchTerm);
      axios({
        url: "https://favqs.com/api/quotes/", 
        method: "GET",
        headers: {
        Authorization: 'Token token="bd63119890a30d433148e0c9297b6c54"'
        },
        params: {
            filter: searchTerm 
        }

        .then(res => {
          this.quotesArray = res.data.quotes;
          console.log(this.quotesArray); 
        })
        .catch(error => console.log(error)), //logging any api errors
      })
    }
  }
})