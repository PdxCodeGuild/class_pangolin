

axios
  .get("https://www.balldontlie.io/api/v1/players?search=doncic")
  .then(res => {
    let playerID = res.data.data[0].id;
    console.log(playerID);
    return axios
      .get(
        `https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]=${playerID}`
      )
      .then(res => {
        console.log(res);
      });
  });
