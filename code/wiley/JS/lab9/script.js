let target = document.getElementById("target");
let quoteBtn = document.getElementById("quoteButton");

//my key: d7d7ed8e461276a16a59d279612c01d2
quoteBtn.addEventListener("click", function(e) {
    axios({
        url:"https://favqs.com/api/qotd",
        method:"GET",

    })
    .then(function(response){
        console.log(response.data);
        console.log(response.data.quote.body);
        console.log(response.data.quote.author);
        let newQuote = 
            `<p><i>${response.data.quote.body}</i></p>
            <p>Spoken by: ${response.data.quote.author}</p>`;
        target.innerHTML = newQuote
    })});
