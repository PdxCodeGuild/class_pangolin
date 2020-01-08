let rainBtn = document.getElementById("tusconRain");
let target = document.getElementById("target");
rainBtn.addEventListener("click", function(e){
    console.log("test");
    axios({
        url:"https://api.openweathermap.org/data/2.5/weather",
        method: "get",
        params:{
            q:"Phoenix",
            APPID:"51e88b6fcb7be7a59ee2655b5605b657"}})
            .then(function(response){
                if (!response.data.rain)console.log("test")
                    target.innerHTML = '<p id="rain">It is NOT raining in Arizona.  Do NOT water your cacti.</p>';
                    let pic = document.createElement("img");
                    pic.src = "noWater.png"
                    pic.id = "dry";
                    target.appendChild(pic);

                if (response.data.rain)console.log(response.data.rain["1h"])
                    target.innerHTML = `<p id="rain">It appears to be raining ${response.data.rain["1h"]} inches an hour in Arizona.  Now is a good time to water your cacti.</p>`;
                    let pic1 = document.createElement("img");
                    pic1.src = "water.jpg";
                    pic1.id = "wet";
                    target.appendChild(pic1);
            })
            .catch(function(err){err => console.log(err)});

})

//to do: add button for changing desired location of rain detector.  Allow user to input a desert like location.  