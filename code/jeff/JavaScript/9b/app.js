let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

quoteButton.addEventListener("click", function(e) {

    axios({
        url: "https://favqs.com/api/quotes",
        method: "GET",
        headers: {
            Authorization: 'Token token="5d668b0c4bebdd61e7278b8eaf14cce5"'
        },

        params: {
            filter: 'funny',
            type: "tag",
        }
    }).then(function(response) {
        let answers = response.data.quotes;
        var funnyQuote = answers[Math.floor(Math.random() * answers.length)];
        let resultHTML = `
        <quote>${funnyQuote.body}</quote>
        <p>${funnyQuote.author}</p>
      `
        let newQuote = document.createElement("p");

        newQuote.innerHTML = resultHTML;
        target.appendChild(newQuote);

    }).catch(function(error) {
        console.log(error);
    })
});