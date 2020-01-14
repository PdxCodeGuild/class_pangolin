
//EXAMPLE OF ASYNCRONIS AXIOS GET CALL.  
axios
  .get("https://www.balldontlie.io/api/v1/players?search=doncic") //getting data object for Luka Doncic
  .then(res => {
    let playerID = res.data.data[0].id; //assigning his ID to playerID
    console.log(playerID);
    return axios //return another axios get call.  
      .get(
        `https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]=${playerID}`
      )
      .then(res => {
        console.log(res);
      });
  });
