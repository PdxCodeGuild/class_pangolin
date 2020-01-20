//DO THIS THING
//FIGURE OUT HOW EMIT WORKS AGAIN


//Luka Doncic playerID = 132
//james Harden playerID = 192
//Giannis Antetokounmpo playerID = 15


Vue.component('playersearch', {
  props: [],
  data: function() {
    return {
      playername: "", 
      playerID: "", 
      playerAverages: [],
      playerfullname: "",
    }
  },

  template: `
  <div>
  <form>
  <input type="text" v-model="playername" placeholder="Search for a player"></input>
  <button id="namesubmit" @click.prevent="getPlayer">Search Player</button>
  </form>
  </div>
  `,
  methods: {
    getPlayer: function() {
    axios.get(`https://www.balldontlie.io/api/v1/players?search=${this.playername}`) //getting data object for searched player
  .then(res => {
    console.log(res);
    // let playerfullname = res.data.data[0].first_name + " " + res.data.data[0].last_name;
    // console.log(playerfullname);
    this.$emit('give-name', res.data.data[0].first_name + " " + res.data.data[0].last_name); //getting full name for display
    let playerID = res.data.data[0].id; //assigning his ID to playerID
    return axios //return another axios get call.  
      .get(
        `https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]=${playerID}`
      )
      .then(response => {
        // console.log(response);
        this.playerAverages.push(response.data.data[0]);
        console.log(this.playerAverages[0]);
        this.$emit('give-player', response.data.data)
      })
  }).catch(error => alert("Player not found.  Check spelling or try using their whole name or only their last name.")); //catch errors and alerts users to change their search parameters
  }
  }
});


let vm = new Vue({
  el: "#app",
  data: {
    playername: "",
    playerfullname: "",
    playerID: "",
    playerAverages: [],
  },
  methods: { 
    logPlayer(x){
      console.log(x); this.playerAverages = x;
  },
    produceName(x) {
      this.playerfullname = x;
    }
  },
  mounted() {}
})