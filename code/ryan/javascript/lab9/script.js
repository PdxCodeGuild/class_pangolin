let getQuote = document.querySelector('#quote-button');
let target = document.querySelector('#target');
let searchText = document.querySelector('#search-text');
let searchButton = document.querySelector('#search-button');

getQuote.addEventListener('click', function(){
    axios({
        url: 'https://favqs.com/api/qotd',
        method: 'GET',
        headers: {
            Authorization: 'Token token="1de4a15a706560aad25ab52cc75e4059"'
        }    
    }).then(function(response){
        let resultHTML =
        `<h3>"${response.data.quote.body}"</h3>
         <p><i>${response.data.quote.author}</i></p>`

        target.innerHTML = resultHTML;
    })  
});  

searchButton.addEventListener('click', function(e){
    console.log('clicked')
    e.preventDefault();
    target.innerHTML = '';
    axios({
        url: "https://favqs.com/api/quotes",
        method: 'GET',
        headers: {
            Authorization: 'Token token="1de4a15a706560aad25ab52cc75e4059"'
        },
        params: {
            filter: searchText.value,
            type: 'tag'
        }
    }).then(function(response){
        let quoteList = response.data.quotes;
        quoteList.forEach(element => {
            let quoteDiv = document.createElement('div');
            quoteDiv.innerHTML =
            `<h3>"${element.body}"</h3>
            <p><em>${element.author}</em></p>`

            target.appendChild(quoteDiv);
            })
            
    })
    searchText.value = '';
}); 
