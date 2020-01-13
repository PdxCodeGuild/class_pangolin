let vm = new Vue({
  el: "#app",
  data: {
    routeInput: "",
    results: []
  },
  methods: {
    getBuses: function() {
      axios({
        method: "get",
        url: "https://developer.trimet.org/ws/v2/vehicles",
        params: {
          appID: apiKey,
          routes: this.routeInput
        }
      }).then(res => this.results = res.data.resultSet.vehicle);
    }
  }
});

/*
secrets.js

let apiKey = "D065A3A5DAE4622752786CEB9";
*/