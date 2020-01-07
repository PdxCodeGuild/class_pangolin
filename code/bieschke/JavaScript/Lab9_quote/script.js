let quoteButton = document.getElementById("quote-button");
let luckyButton = document.getElementById("lucky-button");
let searchButton = document.getElementById("search-button");
let searchButton2 = document.getElementById("search2-button");
let clearButton = document.getElementById("clear-button");
let target = document.getElementById("target");

//gives a random quote
quoteButton.addEventListener("click", function (e) {
    axios({
        method: "GET",
        url: 'https://favqs.com/api/qotd',
        headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
    }).then(function (response) {
        //assigns a tag and class to the output to enable edits later
        let quote = document.createElement("p");
        quote.className = 'quote';
        quote.innerHTML = `${response.data.quote.body} --<i>${response.data.quote.author}</i>`
        target.appendChild(quote);
    }).catch(function (error) {
        console.log('OH YE GODS');
        console.log(error);
    });
});

//searches the database for quotes containing the string 'funny', and returns a random one
luckyButton.addEventListener("click", function (e) {
    axios({
        method: "GET",
        url: 'https://favqs.com/api/quotes/?filter=funny',
        headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
    }).then(function (response) {
        let funny = Math.floor(Math.random() * response.data.quotes.length);
        
        //assigns a tag and class to the output to enable edits later
        let quote = document.createElement("p");
        quote.className = 'quote';
        quote.innerHTML = `
        ${response.data.quotes[funny].body} --<i>${response.data.quotes[funny].author}</i>`
        target.appendChild(quote)
    }).catch(function (error) {
        console.log('OH YE GODS');
        console.log(error);
    });
});

//provides a single quote based on user input
searchButton.addEventListener("click", function (e) {
    let searchTerm2 = document.getElementById("input").value;
    console.log(searchTerm2)
    axios({
        method: "GET",
        url: 'https://favqs.com/api/quotes/?filter=' + searchTerm2,
        headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
    }).then(function (response) {
        let usr = Math.floor(Math.random() * response.data.quotes.length);
        let quote = document.createElement("p");
        quote.className = 'quote';
        quote.innerHTML = `
        ${response.data.quotes[usr].body} --<i>${response.data.quotes[usr].author}</i>`
        target.appendChild(quote)
    }).catch(function (error) {
        console.log('OH YE GODS');
        console.log(error);
    });
});


//provides a list of quotes containing user input
searchButton2.addEventListener("click", function (e) {
    let searchTerm = document.getElementById("input2").value;
    console.log(searchTerm)
    axios({
        method: "GET",
        url: 'https://favqs.com/api/quotes/?filter=' + searchTerm,
        headers: { Authorization: 'Token token="fd782f2f959bb3efad613e037f2ef28b"' }
    }).then(function (response) {
        console.log(response.data)
        let database = response.data.quotes
        console.log(database)

        Array.from(database).forEach(i => {
            let quote = document.createElement("p");
            quote.className = 'quote';
            quote.innerHTML = `${i.body} --<i>${i.author}</i>`
            target.appendChild(quote)
        });
    }).catch(function (error) {
        console.log('OH YE GODS');
        console.log(error);
    });
});

clearButton.addEventListener("click", function (e) {
    let list = document.getElementsByClassName('quote')
    console.log(list)
    Array.from(list).forEach(i => {
        i.remove()
    });
    console.log(list)
});