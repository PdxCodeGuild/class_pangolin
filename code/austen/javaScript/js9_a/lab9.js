let randomBtn = document.getElementById("randomBtn");
let quotes = document.getElementById("quotes");
// let userInput = document.getElementById("text").value;
let submit = document.getElementById("submit");
let clearIt = document.getElementById("clear").style.display = "none";


submit.addEventListener('click',function(e){
    axios({
        url: 'https://favqs.com/api/quotes',
        method: 'get',
        headers: {
            Authorization: 'Token token="542c73b9613a3d9d98ddecbf1257594d"'
        },
        params:{
            filter: document.getElementById("text").value,
            type: 'tag'
        }
    })
    .then(function(response){
        //put in the [0] to identify what one you want to pull the information for.
        // let resultsHTML = `
        // <h3>${response.data.quotes[0].body}</h3>
        // <p>${response.data.quotes[0].author}</p>
        // `;
//the one below gets all and puts all on page
        
        // let clear = document.createElement("button")
        // clear.innerHTML = "Clear"
        // quotes.append(clear);
        document.getElementById("clear").style.display = "block";
        clear.addEventListener('click',function(e){
            while(quotes.firstChild){
                quotes.removeChild(quotes.firstChild);
                document.getElementById("clear").style.display = "none";
            }
        })

        Array.from(response.data.quotes).forEach(element => {
            let resultsHTML = `
            <h4>* ${element.body}</h4>
            <p><em>-- ${element.author}</em></p>
            `;
            let newquote = document.createElement("p");

            newquote.innerHTML = resultsHTML;
            quotes.appendChild(newquote);
        });
       
        console.log(response);
    })
    .catch(function(error){
        console.log(error);
    });
});

randomBtn.addEventListener('click',function(e){
    axios({
        url: 'https://favqs.com/api/qotd',
        method: 'get'
    })
    .then(function(response){

        // let clear = document.createElement("button")
        // clear.innerHTML = "Clear"
        // clearIt.append(clear);
        document.getElementById("clear").style.display = "block";
        clear.addEventListener('click',function(e){
            while(quotes.firstChild){
                quotes.removeChild(quotes.firstChild);
                document.getElementById("clear").style.display = "none";
            }
        })
        let resultsHTML = `
        <h4>* ${response.data.quote.body}</h4>
        <p><em>-- ${response.data.quote.author}</em></p>
        `;
        // console.log(resultsHTML)
        let newquote = document.createElement("p");

        newquote.innerHTML = resultsHTML;
        quotes.appendChild(newquote);
    })
    .catch(function(error){
        console.log(error);
    });
});


