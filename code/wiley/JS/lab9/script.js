let target = document.getElementById("target");
let quoteBtn = document.getElementById("quoteButton");
let clear = document.getElementById("clearQuotes");
let qotdBtn = document.getElementById("qotdBtn");
console.log(qotdBtn);
//VERSION ONE
// my key: d7d7ed8e461276a16a59d279612c01d2
qotdBtn.addEventListener("click", function(e) {
    axios
    .get("https://favqs.com/api/qotd")
    .then(function(response){
        console.log(response.data);
        console.log(response.data.quote.body);
        console.log(response.data.quote.author);
        let newQuote = 
            `<div id="qotdDiv">
            <p><b>Quote of the Day!</b></p>
            <p><i>${response.data.quote.body}</i></p>
            <p>Spoken by: ${response.data.quote.author}</p></div>`;
        target.innerHTML = newQuote;
    })});

//VERSION TWO
quoteBtn.addEventListener("click", function(e){
    axios
    .get("https://favqs.com/api/quotes", {headers:{Authorization: 'Token token="d7d7ed8e461276a16a59d279612c01d2"'},params:{filter: document.getElementById("input").value,type: "tag"}})
    .then(function(response){
        let quotesList = response.data.quotes;
        Array.from(quotesList).forEach(element =>{
            let quote = document.createElement("p");
            quote.className = "quote";
            quote.innerHTML = 
                `<br><i>${element.body}</i> by: ${element.author}`
            target.appendChild(quote);
        })
        console.log(response);
    })
});
clear.addEventListener("click",function(e){
    let quote = document.getElementsByClassName("quote");
    console.log(quote);
    Array.from(quote).forEach(element =>{
        element.remove();
    });
    let Delqotd = document.getElementById("qotdDiv");
    console.log(Delqotd);
    Delqotd.remove();
    });