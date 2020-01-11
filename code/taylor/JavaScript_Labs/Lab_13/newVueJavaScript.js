// Variables
let auth_tk = 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'

// Vue.component('num', {
//     props: ['number'], 
//     template: `<div class="button" @click="$emit('inp', number)" > {{ number }} </div>`
// }); REFEFERENCE


// Vue Components
Vue.component('btn_s1', {
  props: ['btn_s1'], 
  template: `
   
  <button type="" class=" btn btn btn-primary" id="randomSubmit" style="padding: .5rem .5rem .5rem;" onclick="" 
  @click="$emit('inp', number)">{{ button_01 }}</button>
  
  `
});

Vue.component('rCard', {
    props: ['operator'], 
    template:  `
    
    <h4 id="quoteAuthor">{{ author }}</h4>
    <p id="quoteRandom" class="text-black-50 mb-0">{{ body }}</p>
    
    `
});

Vue.component('btn_s2', {
  props: ['number'], 
  template: `
  
  <button type="button" class="btn btn-primary mx-auto" id="searchSubmit" onclick="">
  @click="$emit('inp', number)" {{ button_01 }}</button>
  
  `
});

Vue.component('sCard', {
    props: ['displaylogger'],
    template: `
    
    <div class="col-md-4 mb-3 mb-md-3"></div>
    <div class="card py-4 h-100"></div>
    <div class="card-body text-center"></div>
    <h4 class="text-uppercase m-0 text-wrap">{{ Author }}</h4>
    <div class="small text-black-50">{{ body  }}</div>
    
    `
});

// VUE Root
let vm = new Vue({
  el: "#app",
  data() {
      return {
          button_01 = "Submit", 
          rQuote = {},
          sQuote = [],
          userQuery = "",
          tags = "",
      };
  },
  methods: {

    randomQuote() {
        axios({
        method: "GET",
        url: 'https://favqs.com/api/qotd',
        headers: {
        Authorization: auth_tk}
        }).then(resp => this.rQuote = resp.data.unknownRefAPI);
      },

    searchQoute(userQuery) {
        axios({
        method: 'GET',
        url: 'https://favqs.com/api/quotes',
        headers: {
          Authorization: auth_tk},
        params: { // Parameters for search 
          filter: userQuery, // User input field 
          type: 'tags' // tags represent things like funny, sad, etc.
        }

        }).then(resp => this.sQuote = resp.data.unknownRefAPI);

    },
  }
});
  
