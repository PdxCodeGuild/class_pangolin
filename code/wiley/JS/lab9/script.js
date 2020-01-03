let target = document.getElementById("target");
let quoteBtn = document.getElementById("quoteButton");
//VERSION ONE
//my key: d7d7ed8e461276a16a59d279612c01d2
// quoteBtn.addEventListener("click", function(e) {
//     axios({
//         url:"https://favqs.com/api/qotd",
//         method:"GET",

//     })
//     .then(function(response){
//         console.log(response.data);
//         console.log(response.data.quote.body);
//         console.log(response.data.quote.author);
//         let newQuote = 
//             `<p><i>${response.data.quote.body}</i></p>
//             <p>Spoken by: ${response.data.quote.author}</p>`;
//         target.innerHTML = newQuote
//     })});

//VERSION TWO
quoteBtn.addEventListener("click", function(e){
    axios({
        url:"https://favqs.com/api/quotes",
        method:"GET",
        headers:{
            Authorization: 'Token token="d7d7ed8e461276a16a59d279612c01d2"'
        },
        params: {
            filter: document.getElementById("input").value,
            type: "tag",
        }
    }).then(function(response){
        let quotesList = response.data.quotes;
        Array.from(quotesList).forEach(element =>{
            let quote = document.createElement("p");
            quote.innerHTML = 
                `<br><i>${element.body}</i> by: ${element.author}`
            target.appendChild(quote);
        })
        console.log(response);
    })
})
