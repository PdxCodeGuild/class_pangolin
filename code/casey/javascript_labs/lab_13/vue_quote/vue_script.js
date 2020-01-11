// Vue.component('quote-search', {
//   data: function () {
//     return {
//       searchString: "",
//       body: null,
//       author: null,
//       searchResults: []
//       },
//       axios
//         .get('https://favqs.com/api/quotes', {
//           headers: {
//             Authorization: 'Token token="fa1461cc9347d1fc3065cd7b3eecbf97"'
//           }
//         })
//         .then(response => {
//           this.seachResults = response.data.quotes;
//           // this.body = response.data.quote.body;
//           // this.author = response.data.quote.author;
//         })
//       }
//     });

new Vue({
    el: '#app',
    data () {
      return {
        body: null,
        author: null,
        url: null,
        errored: false,
        loading: false,
        // randomResults: []
      }
    },
    methods: {
      getRandom () {
        axios
          .get('https://favqs.com/api/qotd', {
            headers: {
              Authorization: 'Token token="fa1461cc9347d1fc3065cd7b3eecbf97"'
            }
          })
          .then(response => {
            console.log(response)
            this.body = response.data.quote.body;
            this.author = response.data.quote.author;
            this.url = response.data.quote.url;
          })
          .catch(error => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => this.loading = false);
      }
    }
});