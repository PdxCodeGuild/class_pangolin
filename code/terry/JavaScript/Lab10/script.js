let button = document.getElementById('button');
let result = document.getElementById('result');
let userInput = document.getElementById('userInput');
let pic = document.getElementById('pic');

button.addEventListener('click', myQuote);

function myQuote() {

    axios({
            url: 'https://randomuser.me/api/',
            dataType: 'json',
            success: function(res) {
                console.log(res);
            }
        })
        .then(function(res) {
            console.log(res);
            res.data.results.forEach(function(results) {
                let div_tag = document.createElement('div');
                let node = document.createElement('p');
                let pic_node = document.createElement('p');
                let textnode = document.createTextNode(`${res.data.results[0].name.first} ${res.data.results[0].name.last}`);
                let pic_url = res.data.results[0].picture.large;
                let picnode = document.createElement("img");
                picnode.setAttribute("src", pic_url);
                node.appendChild(textnode);
                pic_node.appendChild(picnode);
                document.getElementById('div_tag').appendChild(div_tag);
                // document.getElementById('result').appendChild(node);
                // document.getElementById('pic').appendChild(pic_node);
                div_tag.appendChild(node);
                div_tag.appendChild(pic_node);
            });
        })
        .catch(function(error) {
            console.log(error);
        });
};