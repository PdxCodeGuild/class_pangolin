let button = document.getElementById("submit");
let clearIt = document.getElementById("clear");
clearIt.style.display= "none";


button.addEventListener('click', function(e){
    axios({
        url: "https://api.openweathermap.org/data/2.5/weather",
        method: "get",
        params:{
            zip:document.getElementById("zip").value,
            units:"imperial",
            APPID:"b028f850ea3341b3c81016a32d4fb757"
        }
    })
    .then(function(response){
        console.log(response)
        let views = document.getElementById("views");
        //clear the value within the box
        zip.value = null;

        let pullData = response.data.weather[0].description;
        let upperData = pullData.toUpperCase();
    
        let resultsHTML = `
        <h2>${response.data.name}</h2>
        <p>${upperData}</p>
        <p>Current Temp: ${Math.round(response.data.main.temp)}&degF</p>
        <p>Feels Like: ${Math.round(response.data.main.feels_like)}&degF</p>
        `;
        let newData = document.createElement("p");

        newData.innerHTML = resultsHTML;
        views.appendChild(newData);
        document.getElementById("submit").style.display = "none";

        clearIt.style.display = "block";
        clearIt.addEventListener('click',function(e){
            while(views.firstChild){
                views.removeChild(views.firstChild);
                
                document.getElementById("clear").style.display = "none";
                document.getElementById("submit").style.display= "block";
            }
            while(tempGuide.firstChild){
                tempGuide.removeChild(tempGuide.firstChild);
            }
        })
        let tempGuide = document.getElementById("tempGuide");
        if (response.data.main.temp>60){
            newTemp = document.createElement("p");
            temp = "<h1><i>You will be fine without a jacket<i></h1>";
            newTemp.innerHTML = temp;
            tempGuide.appendChild(newTemp)
        }
        else{
            newTemp = document.createElement("p");
            temp = "<h1><i>I would recommend a jacket<i></h1>";
            newTemp.innerHTML = temp;
            tempGuide.appendChild(newTemp)
        }
    })
    .catch(function(error){
        console.log(error)
    });
})