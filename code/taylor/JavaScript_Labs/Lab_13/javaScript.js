// Variables
let auth_tk = 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'

// Vue Components

// Random quote button
Vue.component('btn_s1', {
 
  template: `

  <button 
  class=" btn btn-primary" 
  id="randomSubmit"  
  @click="$emit('r1submit')">Submit</button>
  
  `
});

// Random quote card display 
Vue.component('rcard', {
   
  template:  `
  <div>

    <h4 
    id="quoteAuthor">
    {{ this.$root.$data.result.author }}
    </h4>
  
    <p 
    id="quoteRandom" 
    class="text-black-50 mb-0">
    {{ this.$root.$data.result.body }}
    </p>

  </div>
  `
});

// Search for "tagged" quotes, returns 25 quote cards 
Vue.component('scard', {
  data:function(){
      return{
      userQuery: '',
      quoteArray: []
      }
  },
  
// Template to display 25 searched card returns
  template: `
  <div> <!-- Template Div -->

  <!-- Search Quote Section -->
    <section id="signup" class="signup-section">
      <div class="container">
        <div class="row">
          <div class="col-md-10 col-lg-8 mx-auto text-center">
            <h2 class="text-white mb-5">Enter a search term and find your next Quote!</h2>
            <form class="form-inline d-flex">

              <input type="text" class="form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0" id="inputSearch" maxlength="30" v-model="userQuery"  placeholder="Search term here...">
              
              <button type="button" class="btn btn-primary mx-auto" id="searchSubmit" @click.prevent="searchQuote">Submit</button>

            </form>
          </div>
        </div>
      </div>
    </section>

  <!-- Quotes Display Section -->

  <section class="contact-section bg-black">
  <div class="container">
    <div id="allQuotes"class="row">

       <div class="col-md-4 mb-3 mb-md-3" v-for="quote in quoteArray">
        <div class="card py-4 h-100" >
          <div class="card-body text-center">
            <h4 class="text-uppercase m-0 text-wrap">{{ quote.author }}</h4>
            <div class="small text-black-50">{{ quote.body  }}</div>
          </div>
        </div>
      </div>

      </div>
      <div class="social d-flex justify-content-center">
        <a href="#" class="mx-2">
          <i class="fab fa-github"></i>
        </a>
      </div>
    </div>

  </section>
</div>
  `,
// Search for a tagged quote method
  methods:{
    searchQuote: function() {
        axios({
            method:"get",
            url:"https://favqs.com/api/quotes/",
            headers:{
                Authorization: auth_tk
            },
            params: {
                filter: this.userQuery,
                type: 'tag',
            }
        })
        .then(response => {(this.quoteArray = response.data.quotes);
        })
      }
    }     
  });

// Vue root
let vm = new Vue({
  el: '#app',
  data: {
   result: {}
  },

  // Return random qoute upon submit click
  methods: {
    randomQuote() {
        axios({
        method: "GET",
        url: 'https://favqs.com/api/qotd/',
      }).then(response => {(this.result = response.data.quote)})
    },
  },
});
