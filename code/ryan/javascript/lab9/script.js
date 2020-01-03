let getQuote = document.querySelector('#quote-button');
let target = document.querySelector('#target');

getQuote.addEventListener('click', function(){
    axios({
        url: 'https://favqs.com/api/qotd',
        method: 'GET',
        headers: {
            Authorization: 'Token token="1de4a15a706560aad25ab52cc75e4059"'
        }    
    }).then(function(response){
        let resultHTML =
        `<p>${response.data.quote.body}</p>
         <p><i>${response.data.quote.author}</i></p>`

        target.innerHTML = resultHTML;
    })  
});       
    
