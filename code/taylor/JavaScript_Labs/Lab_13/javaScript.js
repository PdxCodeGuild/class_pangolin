// Bot nom nom 44462dcda4bba9533e2d37b1b089f7b5

let responseData = {};

//  Function API call for a single random quote
function callForRandomQuote (){
  axios({
  method: 'GET',
  url: 'https://favqs.com/api/qotd',
  headers: {
    Authorization: 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'
  }
})
  .then(function (response) {
    responseData = response.data;
    return responseData
  })
  .catch(function (error) {
    // handle error
    console.log(error);
})};

// Runs single random quote API call to preoad a random qote
callForRandomQuote()

// "RANDOM" button for random quote page load
let randomSubmit = document.getElementById('randomSubmit');

// "RANDOM" button onlclik listner
randomSubmit.onclick = function() {
  callForRandomQuote() // Reloads randomData with a new data / quote object
  postRandomQuote(responseData) // Call to post a random qoute
   
};

// Function to post a random quote
function postRandomQuote(responseData) {

  // Retreives allQoutes element as target for appends
  let quoteAuthor = document.getElementById('quoteAuthor')
  let quoteRandom = document.getElementById('quoteRandom')
   
    // Adds content to the html build
    quoteAuthor.innerText = responseData.quote.author;
    quoteRandom.innerText = responseData.quote.body;
    // Replaces the respective DOM text
    quoteAuthor.replaceWith(quoteAuthor);
    quoteRandom.replaceWith(quoteRandom);
  }

// User input field for quote search by key term
let userQuery = document.getElementById('inputSearch')
// QTRIEVE button next to searchinput field
let searchSubmit = document.getElementById('searchSubmit');

// QTRIEVE button onclick listener
searchSubmit.onclick = function() {
  searchForAQuote(userQuery.value)
};

//  Function API call for a single random quote
function searchForAQuote (userQuery){
  axios({
  method: 'GET',
  url: 'https://favqs.com/api/quotes',
  headers: {
    Authorization: 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'
  },
  params: { // Parameters for search 
    filter: userQuery, // User input field 
    type: 'tags' // tags represent things like funny, sad, etc.
  }
})
  .then(function (response) {
          
         let searchArray = Array.from(response.data.quotes);

         searchArray.forEach(element => {
          buildSearchedQuoteCards(element.author, element.body)
          console.log(element.author, element.body)
        });
         

  })
  .catch(function (error) {
    // handle error
    console.log(error);
})};

// Funciton to build author / quote cards from search
function buildSearchedQuoteCards(author, quote) {

// Retreives allQoutes element as target for appends
  let allQuotes = document.getElementById('allQuotes')

// Builds the div / card for all qoutes
  let div_1 = document.createElement("div");
  div_1.className = "col-md-4 mb-3 mb-md-3";
  allQuotes.appendChild(div_1)
  let div_2 = document.createElement('div');
  div_2.className = "card py-4 h-100";
  div_1.appendChild(div_2)
  let div_3 = document.createElement('div');
  div_3.className = "card-body text-center";
  div_2.appendChild(div_3)

// Builds the html recepticles for qoute author and qote
  let h4 = document.createElement('h4');
  h4.className = "text-uppercase m-0 text-wrap";
  div_3.appendChild(h4);
  let div_4 = document.createElement('div');
  div_4.className = "small text-black-50";
  div_3.appendChild(div_4)

// Adds content to the html build
  h4.innerHTML = author;
  div_4.innerHTML = quote;
};



let vm = new Vue({
  el: "#app",
  data: {
    routeInput: "",
    results: []
  },
  methods: {
    getBuses: function() {
      axios({
        method: "get",
        url: "https://developer.trimet.org/ws/v2/vehicles",
        params: {
          appID: apiKey,
          routes: this.routeInput
        }
      }).then(res => this.results = res.data.resultSet.vehicle);
    }
  }
});

/*
secrets.js

let apiKey = "D065A3A5DAE4622752786CEB9";
*/