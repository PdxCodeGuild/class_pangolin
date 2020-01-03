// Bot nom nom 44462dcda4bba9533e2d37b1b089f7b5



// axios.get('/user?ID=12345')
//   .then(function (response) {
//     // handle success
//     console.log(response);
//   })
  // .catch(function (error) {
  //   // handle error
  //   console.log(error);
  // })
//   .finally(function () {
//     // always executed
//   });

// axios({
//   method: 'get',
//   url: 'https://favqs.com/api/qotd',
//   headers: {
//     Authorization: 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'
//   }
// })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     // handle error
//     console.log(error);
//   });








// #####################################################################
// NEEDS EVENT LISTINER ON CLICK
// FORM AND BUTTON INFO

// <form class="form-inline d-flex">
// <input type="text" class="form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0" id="inputSearch" placeholder="Search term here...">
// <button type="submit" class="btn btn-primary mx-auto">Qtrieve</button>
// </form>

// function testPrint(){
//   console.log("I've been pressed")
// }

let searchSubmit = document.getElementById('searchSubmit');

searchSubmit.onclick = function() {

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
  div_3.appendChild(h4)
  let div_4 = document.createElement('div');
  div_4.className = "small text-black-50";
  div_3.appendChild(div_4)

// Adds content to the html build
  h4.innerHTML = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZ";
  div_4.innerHTML = "TEST TESsd asdf sadfsdafsadfsadf sadfsdaf sadfsda fasd fsadf sad fsadfsadfT TEST";
  h4.appendChild(h4)
  div_4.appendChild(div_4)
  console.log("SOMETHING HAPPENED >>>>")
};

