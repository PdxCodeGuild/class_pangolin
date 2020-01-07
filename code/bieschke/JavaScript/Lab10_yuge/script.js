let randButton = document.getElementById("rand-button");
let armsButton = document.getElementById("arms-button");
let searchButton = document.getElementById("search-button");
let searchButton2 = document.getElementById("search2-button");
let clearButton = document.getElementById("clear-button");
let target = document.getElementById("target");

randButton.addEventListener("click", function(e) {
    axios({
        method: 'GET',
        url: "https://wger.de/api/v2/exercise",
        headers: { 
            Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6' }
    }).then(function (response) {
        console.log(response)
        let angles = response.data.results.filter(function(item) {
            console.log(item)
            return item.language === 2 && item.name;    //sorts named responses in english
        });
        console.log(angles)
        //document.getElementById().innerHTML = response.filter(angles)

        let bacon = Math.floor(Math.random() * angles.length);

        let eggs = document.createElement("p");
        eggs.className = 'eggs';
        eggs.innerHTML = `${angles[bacon].name}\n ${angles[bacon].description}`
        target.appendChild(eggs);
        console.log(angles[bacon]);
    });
});

armsButton.addEventListener("click", function (e) {
    axios({
        method: 'GET',
        url: "https://wger.de/api/v2/exercise",
        headers: { 
            Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6' }
    }).then(function (response) {
        let arms = response.data.results.filter(function(item) {
            console.log(item)
            return item.name === 'Arms';    
        });
        let bacon = Math.floor(Math.random() * arms.length);
        console.log(arms.length);
        let eggs = document.createElement("p");
        eggs.className = 'eggs';
        eggs.innerHTML = `${arms[bacon].name}\n ${arms[bacon].description}`
        target.appendChild(eggs);
        console.log(arms[bacon]);

    })
})