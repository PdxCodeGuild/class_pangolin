// get DOM elements
let quote = document.getElementById("quote");
let author = document.getElementById("author");
let nextButton = document.getElementById("next-quote");

// Axios API call
axios.defaults.baseURL = 'https://favqs.com/api/';

// load default quote
axios.get("qotd")
    .then(function (response) {
        console.log(response.data);
        quote.innerText = response.data["quote"]["body"];
        author.innerText = response.data.quote.author;
    })

// next button event listener for new quote
nextButton.addEventListener('click', function () {
    axios.get("qotd")
        .then(function (response) {
            console.log(response.data);
            quote.innerText = response.data["quote"]["body"];
            author.innerText = response.data.quote.author;
        })
});