// Bot nom nom 44462dcda4bba9533e2d37b1b089f7b5


// axios.get('/user?ID=12345')
//   .then(function (response) {
//     // handle success
//     console.log(response);
//   })
//   .catch(function (error) {
//     // handle error
//     console.log(error);
//   })
//   .finally(function () {
//     // always executed
//   });

axios({
  method: 'get',
  url: 'https://favqs.com/api/qotd',
  headers: {
    Authorization: 'Token token="44462dcda4bba9533e2d37b1b089f7b5"'
  }
})
  .then(function (response) {
    console.log(response)
  });



// #####################################################################
// NEEDS EVENT LISTINER ON CLICK
// FORM AND BUTTON INFO

// <form class="form-inline d-flex">
// <input type="text" class="form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0" id="inputSearch" placeholder="Search term here...">
// <button type="submit" class="btn btn-primary mx-auto">Qtrieve</button>
// </form>



// #####################################################################
// NEEDS TO BUILD THESE AS QOUTE OUTPUT

//       <div id="allQuotes"class="row">


//       <div class="col-md-4 mb-3 mb-md-0">
//         <div class="card py-4 h-100">
//           <div class="card-body text-center">

//             <h4 class="text-uppercase m-0">Quote Author</h4>
//             <hr class="my-4">
//             <div class="small text-black-50">QUOTE - Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate animi itaque vel quo saepe? Similique corrupti laudantium veniam magni? Asperiores maxime suscipit aliquam aut sit adipisci possimus voluptatum. Voluptatem, harum?</div>
//           </div>
//         </div>
//       </div>
