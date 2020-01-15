let vm = new Vue({
  el: "#app",
  data: {
    question: '',
    answer: '',
    category: '',
    clicked: false,
  },
  methods: {
    showAnswer: function() {
      this.clicked = !this.clicked;
    },
    getRandomQuestion: function() {
      this.clicked = false;
      axios({
        url: "http://jservice.io/api/random", 
        method: "GET",
        params: {
          
        }})
        .then( (response) => {
        console.log(response.data)
        this.question = response.data[0].question;
        this.answer = response.data[0].answer;
        this.category = response.data[0].category.title;
        console.log(response.data)
        })
        .catch(function (error) {
          this.results.push("no results")
        })
    }
  }
});

