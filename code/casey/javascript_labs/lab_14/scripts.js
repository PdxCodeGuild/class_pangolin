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
                    appID: "D065A3a5DAE4622752786CEB9",
                    routes: this.routeInput
                }
            }).then(res => this.results = res.data.resultsSet.vehicle);
            
        }
    }
});