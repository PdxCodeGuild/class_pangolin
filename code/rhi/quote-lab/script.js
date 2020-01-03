let button = document.getElementById("quote-button");
let target = document.getElementById("target");

// get the info from the api
button.addEventListener("click", function(e) {
    axios({
        url: "https://favqs.com/api/qotd",
        method: "GET",
        headers: {
            Authorization: 'Token token= "50f3400c99d67bd71bea7d473c15ce73"'
        }
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