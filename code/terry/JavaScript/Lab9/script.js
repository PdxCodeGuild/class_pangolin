let button = document.getElementById('button');
let result = document.getElementById('result');
let userInput = document.getElementById('userInput');

button.addEventListener('click', myQuote);

function myQuote() {
    let input = userInput.value;
    axios({
            url: 'https://favqs.com/api/quotes',
            method: 'GET',
            headers: {
                Authorization: 'Token token="898ce244ffea7807a375ce02f5a27f99"'
            },
            params: {

                filter: input,
                // type: 'tags'
            },
        })
        .then(function(response) {
            console.log(response);
            Array.from(response.data.quotes).forEach(function(quote) {
                // let pageInput = `${quote.body}<p><em>--${quote.author}</em></p>`;
                // result.innerHTML = pageInput;
                let node = document.createElement('p');
                let textnode = document.createTextNode(`${quote.body} --${quote.author}`);
                node.appendChild(textnode);
                document.getElementById('result').appendChild(node);

            });

        })
        .catch(function(error) {
            console.log(error);
        });
};