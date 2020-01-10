let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

    quoteButton.addEventListener("click", function(e) {
        var input = document.getElementById("input").value
        var searchTerm = encodeURIComponent(input);
        console.log(searchTerm)
        axios({
        url: "https://favqs.com/api/quotes/",
        
        method: "GET",
        headers: {
        Authorization: 'Token token="bd63119890a30d433148e0c9297b6c54"'
        },
        params: {
            filter: searchTerm 
        }
    }).then(function(response){

        let database = response.data.quotes;
        console.log(database)
        target.innerHTML = ``

        Array.from(database).forEach(i => {
            let quote = document.createElement("p");
            quote.className = 'quote';
            quote.innerHTML = `
            ${i.body} --<i>${i.author}</i>
            `
            target.appendChild(quote)
        })
    }).catch(function(error){
        console.log(error);
    })
});