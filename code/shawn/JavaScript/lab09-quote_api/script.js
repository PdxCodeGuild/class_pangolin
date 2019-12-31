// get DOM elements
let quote = document.getElementById("quote");
let quoteList = document.getElementById("quote-list");
let author = document.getElementById("author");
let nextButton = document.getElementById("next-quote");
let pageId = document.getElementById("pages");
let keywords = document.getElementById("keywords");
let filterButton = document.getElementById("filter-button");
let pageButton = document.getElementById("page-button");

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

// api key kept in local file secrets.txt, remove before pushing to remote
let api_key = '';
// query API
let config = {
    headers: {
        'Authorization': `Token token=${api_key}`
    }
}

// page load list
axios.get(`quotes?page=1`, config)
    .then(function (response) {
        console.log(response.data)
        // loop throuh each quote
        for (let quote of response.data.quotes) {
            let newQuoteDiv = document.createElement("div");
            let newQuoteText = document.createElement("p");
            let newQuoteAuthor = document.createElement("p");
            newQuoteDiv.classList.add("list-quote-div");
            newQuoteText.classList.add("list-quote-text");
            newQuoteAuthor.classList.add("list-quote-author");
            newQuoteText.innerText = quote.body
            newQuoteAuthor.innerText = "-" + quote.author;
            newQuoteDiv.append(newQuoteText);
            if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
            quoteList.append(newQuoteDiv);

        }
    })



// get a list of quotes, updated when filter boxes are changed
filterButton.addEventListener('click', function () {
    // clear current quoteList
    pageId.value=1;
    quoteList.innerHTML = '';
    // if filter is blank, omit from URL
    if (!keywords.value) {
        axios.get(`quotes?page=${pageId.value}`, config)
            .then(function (response) {
                console.log(response.data)
                // loop throuh each quote
                for (let quote of response.data.quotes) {
                    let newQuoteDiv = document.createElement("div");
                    let newQuoteText = document.createElement("p");
                    let newQuoteAuthor = document.createElement("p");
                    newQuoteDiv.classList.add("list-quote-div");
                    newQuoteText.classList.add("list-quote-text");
                    newQuoteAuthor.classList.add("list-quote-author");
                    newQuoteText.innerText = quote.body
                    newQuoteAuthor.innerText = "-" + quote.author;
                    newQuoteDiv.append(newQuoteText);
                    if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                    quoteList.append(newQuoteDiv);

                }
            })
    } else {
        axios.get(`quotes?page=${pageId.value}&filter=${encodeURIComponent(keywords.value)}`, config)
            .then(function (response) {
                // loop throuh each quote
                for (let quote of response.data.quotes) {
                    let newQuoteDiv = document.createElement("div");
                    let newQuoteText = document.createElement("p");
                    let newQuoteAuthor = document.createElement("p");
                    newQuoteDiv.classList.add("list-quote-div");
                    newQuoteText.classList.add("list-quote-text");
                    newQuoteAuthor.classList.add("list-quote-author");
                    newQuoteText.innerText = quote.body
                    newQuoteAuthor.innerText = "-" + quote.author;
                    newQuoteDiv.append(newQuoteText);
                    if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                    quoteList.append(newQuoteDiv);

                }
            })
    }
})

pageId.addEventListener('input', function () {
    // clear current quoteList
    quoteList.innerHTML = '';
    // if filter is blank, omit from URL
    if (!keywords.value) {
        axios.get(`quotes?page=${pageId.value}`, config)
            .then(function (response) {
                console.log(response.data)
                // loop throuh each quote
                for (let quote of response.data.quotes) {
                    let newQuoteDiv = document.createElement("div");
                    let newQuoteText = document.createElement("p");
                    let newQuoteAuthor = document.createElement("p");
                    newQuoteDiv.classList.add("list-quote-div");
                    newQuoteText.classList.add("list-quote-text");
                    newQuoteAuthor.classList.add("list-quote-author");
                    newQuoteText.innerText = quote.body
                    newQuoteAuthor.innerText = "-" + quote.author;
                    newQuoteDiv.append(newQuoteText);
                    if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                    quoteList.append(newQuoteDiv);

                }
            })
    } else {
        axios.get(`quotes?page=${pageId.value}&filter=${encodeURIComponent(keywords.value)}`, config)
            .then(function (response) {
                // loop throuh each quote
                for (let quote of response.data.quotes) {
                    let newQuoteDiv = document.createElement("div");
                    let newQuoteText = document.createElement("p");
                    let newQuoteAuthor = document.createElement("p");
                    newQuoteDiv.classList.add("list-quote-div");
                    newQuoteText.classList.add("list-quote-text");
                    newQuoteAuthor.classList.add("list-quote-author");
                    newQuoteText.innerText = quote.body
                    newQuoteAuthor.innerText = "-" + quote.author;
                    newQuoteDiv.append(newQuoteText);
                    if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                    quoteList.append(newQuoteDiv);

                }
            })
    }
})

keywords.addEventListener('keydown', function (e) {
    if (e.code === "Enter") {
        pageId.value=1;
        // clear current quoteList
        quoteList.innerHTML = '';
        // if filter is blank, omit from URL
        if (!keywords.value) {
            axios.get(`quotes?page=${pageId.value}`, config)
                .then(function (response) {
                    console.log(response.data)
                    // loop throuh each quote
                    for (let quote of response.data.quotes) {
                        let newQuoteDiv = document.createElement("div");
                        let newQuoteText = document.createElement("p");
                        let newQuoteAuthor = document.createElement("p");
                        newQuoteDiv.classList.add("list-quote-div");
                        newQuoteText.classList.add("list-quote-text");
                        newQuoteAuthor.classList.add("list-quote-author");
                        newQuoteText.innerText = quote.body
                        newQuoteAuthor.innerText = "-" + quote.author;
                        newQuoteDiv.append(newQuoteText);
                        if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                        quoteList.append(newQuoteDiv);

                    }
                })
        } else {
            axios.get(`quotes?page=${pageId.value}&filter=${encodeURIComponent(keywords.value)}`, config)
                .then(function (response) {
                    // loop throuh each quote
                    for (let quote of response.data.quotes) {
                        let newQuoteDiv = document.createElement("div");
                        let newQuoteText = document.createElement("p");
                        let newQuoteAuthor = document.createElement("p");
                        newQuoteDiv.classList.add("list-quote-div");
                        newQuoteText.classList.add("list-quote-text");
                        newQuoteAuthor.classList.add("list-quote-author");
                        newQuoteText.innerText = quote.body
                        newQuoteAuthor.innerText = "-" + quote.author;
                        newQuoteDiv.append(newQuoteText);
                        if (quote.body != "No quotes found") newQuoteDiv.append(newQuoteAuthor);
                        quoteList.append(newQuoteDiv);

                    }
                })
        }
    }
})