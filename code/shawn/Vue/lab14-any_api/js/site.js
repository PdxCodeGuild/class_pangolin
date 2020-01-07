let app = new Vue({
    el: "#app",
    data: {
        ship: "Hello Vue.js",
        selectedLeagueText: "Hurricane",
        selectedLeagueNum: 0,
        realm: 'na',
        seasonNumber: 7,
        clans: []
    },
    methods: {
        selectLeague: function (league) {
            if (league == "hurricane") {
                this.selectedLeagueText = "Hurricane";
                this.selectedLeagueNum = 0;
            } else if (league == "typhoon") {
                this.selectedLeagueText = "Typhoon";
                this.selectedLeagueNum = 1;
            } else if (league == "storm") {
                this.selectedLeagueText = "Storm";
                this.selectedLeagueNum = 2;
            } else if (league == "gale") {
                this.selectedLeagueText = "Gale";
                this.selectedLeagueNum = 3;
            } else if (league == "squall") {
                this.selectedLeagueText = "Squall";
                this.selectedLeagueNum = 4;
            }
            this.displayLeague();
        },
        displayLeague: function () {
            let url; 
            if (this.selectedLeagueNum == 0) {
                console.log("returning hurricane")
                url = `https://clans.worldofwarships.com/clans/wows/ladder/api/structure/?season=${this.seasonNumber}&realm=${this.realm}`;
            } else if (this.selectedLeagueNum == 1) {
                url = `https://clans.worldofwarships.com/clans/wows/ladder/api/structure/?season=${this.seasonNumber}&realm=${this.realm}&league=1&division=1`
            } else if (this.selectedLeagueNum == 2) {
                url = `https://clans.worldofwarships.com/clans/wows/ladder/api/structure/?season=${this.seasonNumber}&realm=${this.realm}&league=1&division=1`
            } else if (this.selectedLeagueNum == 3) {
                url = `https://clans.worldofwarships.com/clans/wows/ladder/api/structure/?season=${this.seasonNumber}&realm=${this.realm}&league=1&division=1`
            } else if (this.selectedLeagueNum == 4) {
                url = `https://clans.worldofwarships.com/clans/wows/ladder/api/structure/?season=${this.seasonNumber}&realm=${this.realm}&league=1&division=1`
            }
            axios.get(url)
            .then(function (response) {
              console.log(response.data)
            })
            
        }
    },
});