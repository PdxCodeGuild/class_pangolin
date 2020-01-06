let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

quoteButton.addEventListener("click", function(e) {

    axios({
        url: "https://favqs.com/api/qotd",
        method: "GET",
        headers: {
            Authorization: 'Token token = "5d668b0c4bebdd61e7278b8eaf14cce5"'
        }
    }).then(function(response) {
        let resultHTML = `
        <p>${response.data.quote.body}</p>
        <p><i><a href="${response.data.quote.url}">${response.data.quote.author}</a></i></p>
      `
        let newQuote = document.createElement("p");

        newQuote.innerHTML = resultHTML;
        target.appendChild(newQuote);
        textTarget.innerHTML = resultHTML;
        console.log(resultHTML)
    }).catch(function(error) {
        console.log(error);
    })
});