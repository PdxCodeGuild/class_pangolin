let button = document.getElementById("quote-button");
let target = document.getElementById("target");
let option = document.getElementById("option");
let option_btn = document.getElementById("option-btn")
let option_result = document.getElementById("option-result")

// get the info from the api
button.addEventListener("click", function(e) {
    axios({
        url: "https://favqs.com/api/qotd",
        method: "GET",
        headers: {
            Authorization: 'Token token="50f3400c99d67bd71bea7d473c15ce73"'
        },

        // render the info into the HTML page so it can be seen on webpage
    }).then(function(response){
        let resultHTML = `
        <p>${response.data.quote.body}</p>
        <p><i><a href="${response.data.quote.url}">${response.data.quote.author}</a></i></p>
        `
        target.innerHTML = resultHTML;

        // log the errors in the console.log so that you can see what went wrong
    }).catch(function(error) {
        console.log(error);
    })
}); 

// get the info from the api
option_btn.addEventListener("click", function(e) {
    axios({
        url: "https://favqs.com/api/quotes",
        method: "GEt",
        headers: {
            Authorization: 'Token token="50f3400c99d67bd71bea7d473c15ce73"'
        },

        params: {
            filter: option.value,
            type: "tag",
        }

        // render the info into the HTML page so it can be seen on webpage
    }).then(function(response){
        let answers = response.data.quotes;
        let filterquote = answers[Math.floor(Math.random() * answers.length)];
        console.log(filterquote)
        let resultHTML = `
        <p>${filterquote.body}</p>
        <p><i><a href="${filterquote.url}">${filterquote.author}</a></i></p>
        `
        option_result.innerHTML = resultHTML;
        console.log(option)
        // log the errors in the console.log so that you can see what went wrong
    }).catch(function(error) {
        console.log(error);
    })
}); 