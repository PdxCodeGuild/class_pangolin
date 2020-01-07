let quoteButton = document.getElementById("quote-button");
let searchButton = document.getElementById("search-button");
let search = document.getElementById("search");
let target = document.getElementById("target");

quoteButton.addEventListener("click", function(e) {
    e.preventDefault();
    axios({
        url: "https://favqs.com/api/qotd", 
        method: "GET",
        headers: {
            Authorization: 'Token token="fa1461cc9347d1fc3065cd7b3eecbf97"'
        }
    }).then(function(response) {
        let resultHTML = `
        <p "quote-display"><i>"${response.data.quote.body}"</i></p>
        <p "quote-display"><i><a href="${response.data.quote.url}">${response.data.quote.author}</a></i></p>
        `
        target.innerHTML = resultHTML;
    }).catch(function(error) {
        console.log(error);
    })
});

searchButton.addEventListener("click", function(e) {
    e.preventDefault();
    axios({
        url: "https://favqs.com/api/quotes",
        method: "GET",
        headers: {
            Authorization: 'Token token="fa1461cc9347d1fc3065cd7b3eecbf97"'
        },
        params: {
            filter: search.value,
            type: "tag",
        }
    }).then(function(response) {
        let quotes = response.data.quotes;
        Array.from(quotes).forEach(quote =>{
            console.log(quote);
            let resultHTML = `
            <p id="quote-display"><i>"${quote.body}"</i></p>
            <p "quote-display"><i><a href="${quote.url}">${quote.author}</a></i></p>
            `
            target.innerHTML = resultHTML;
        });
    }).catch(function(error) {
        console.log(error);
    });
});
// 'Authorization: Token token="fa1461cc9347d1fc3065cd7b3eecbf97"'