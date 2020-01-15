let submitButton = document.getElementById("submit");
let target = document.getElementById("target");

    submitButton.addEventListener("click", function(e) {
        var input = document.getElementById("input").value
        var searchTerm = encodeURIComponent(input);
        console.log(searchTerm)
        axios({
        url: "http://countryapi.gear.host/v1/Country/getCountries?pName=" + searchTerm,
        
        method: "GET",
        params: {
            filter: searchTerm 
        }
    }).then(function(response){

        let database = response.data;
        console.log(database)
        let result = `
            <h3>${response.Name}</h3><br>
            <p>Native name: ${response.NativeName}</p>
            <p>Region: ${response.Region}</p>
            `
            target.innerHTML = result

    }).catch(function(error){
        console.log(error);
    })
});