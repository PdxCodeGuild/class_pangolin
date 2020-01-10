Vue.component("byauthor", {
  data: function() {
    return { author: "", quotesArray: [],headerAuthor: "" };
  },
  template: `<div>
        <form>
        <input type="text" v-model='author' placeholder="Search by author"></input>
        <button @click.prevent="getauthor" id="submit">submit</button>
        </form>
        <div v-show='quotesArray.length === 0'> No quotes found yet </div>
        <ul v-if='quotesArray.length >0'>
        <h3> Here are some quotes by: {{this.headerAuthor}} </h3>
        <li v-for="quote in quotesArray" id="quotes">
        {{ quote.body }}
        </li>
        </ul>
        </div>`,

  methods: {
    getauthor: function() {
      console.log(this.author);
      axios({
        url: "https://favqs.com/api/quotes",
        method: "get",
        headers: {
          Authorization: 'Token token="d7d7ed8e461276a16a59d279612c01d2"'
        },
        params: {
          filter: this.author,
          type: "author"
        }
      })
        .then(res => {
          this.quotesArray = res.data.quotes;
          this.headerAuthor = this.author;
          console.log(this.quotesArray);
        })
        .catch(error => console.log(error));
    }
  }
});

let vm = new Vue({
  el: "#app",
  data: {
    qotd: "TEST",
    keyword: "",
    // author: "",
    tag: ""
  },
  methods: {},
  mounted() {
    axios.get("https://favqs.com/api/qotd").then(res => {
      this.qotd = res.data.quote;
    });
  }
});
