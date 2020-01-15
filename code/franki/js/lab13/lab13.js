Vue.component('quote-detail', {
  props: [],
  data: function() {
    return {
      quote: '',
      author: '',
    }
  },
  template: `
  <div class="quote" v-for="result in searchResults">{{ quote }}</div>
  <div>{{ author }}</div>
  `
});

let vm = new Vue({
  el: '#app',
  data: {
    searchTerm: '',
    searchResults: [],
  },
  methods: {
    searchQuotes: function() {
      var input = document.getElementById("input").value
      var searchTerm = encodeURIComponent(input);
      console.log(searchTerm)
      axios({
        url: "https://favqs.com/api/quotes/", 
        method: "GET",
        headers: {
        Authorization: 'Token token="bd63119890a30d433148e0c9297b6c54"'
        },
        params: {
            filter: searchTerm 
        }
      })
    }
  }
})