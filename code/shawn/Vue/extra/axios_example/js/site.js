// apiKey is in secrets.js

let vm = new Vue({
    el: "#app",
    data: {
        routeInput: "",
        results: [],
    },
    methods: {
        getBuses: function(){
            axios( {
                method: "get",
                url: "https://developer.trimet.org/ws/v2/vehicles",
                params: {
                    appID: apiKey,
                    routes: this.routeInput
                }
            }).then(res => this.results = res.data.resultSet.vehicle);  //needs to be arrow function so we can refer to axios
                
        }
    }
});