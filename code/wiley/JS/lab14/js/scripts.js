//DO THIS THING
//FIGURE OUT HOW EMIT WORKS AGAIN


//Luka Doncic playerID = 132
//james Harden playerID = 192
//Giannis Antetokounmpo playerID = 15


Vue.component('playersearch', {
  props: ['thing'],
  data: function() {
    return {
      playername: "", 
      playerID: "", 
      playerAverages: []
    }
  },

  template: `
  <div>
  <form>
  <input type="text" v-model="playername" placeholder="Search for a player"></input>
  <button id="namesubmit" @click.prevent="$emit('getPlayer')">Search Player</button>
  </form>
  </div>
  `,
  methods: {
    getPlayer: function() {
    axios.get(`https://www.balldontlie.io/api/v1/players?search=${this.playername}`) //getting data object for searched player
  .then(res => {
    let playerID = res.data.data[0].id; //assigning his ID to playerID
    // console.log(playerID);
    return axios //return another axios get call.  
      .get(
        `https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]=${playerID}`
      )
      .then(res => {
        this.playerAverages.push(res.data.data[0]);
        console.log(res);
        console.log(this.playerAverages[0]);
      })
  });
  }
  }
});


let vm = new Vue({
  el: "#app",
  data: {
    playername: "",
    playerID: "",
    playerAverages: [],
  },
  methods: {},
  mounted() {}
})