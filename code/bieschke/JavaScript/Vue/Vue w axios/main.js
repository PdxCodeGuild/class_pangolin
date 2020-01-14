let vm = new Vue({
    el: "#app",
    data: {
        routeInput: '',
        results: []
    },
    methods: {
        getBuses: function() {
            axios({
                method: "GET",
                url: "https://developer.trimet.org/ws/v2/vehicles",
                params: {
                    appID: "D065A3A5DAE4622752786CEB9",
                    routes: this.routeInput
                }
            }).then(res => this.results = res.data.resultSet.vehicle);
            //an arrow function doesn't reassign this, like a traditional function
        }
    }
});