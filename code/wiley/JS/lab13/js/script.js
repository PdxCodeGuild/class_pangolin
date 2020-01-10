Vue.component("byauthor", {
  data: function() {
    return { author: "", quotesArray: [] };
  },
  template: `<div>
        <form>
        <input type="text" v-model='author' placeholder="Search by author"></input>
        <button @click.prevent="getauthor">submit</button>
        </form>
        <div v-show='quotesArray.length === 0'> No quotes found yet </div>
        <ul v-if='quotesArray.length >0'>
        <li v-for="quote in quotesArray">
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
      .then(res => {this.quotesArray = res.data.quotes;
    console.log(this.quotesArray)}
        );
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
