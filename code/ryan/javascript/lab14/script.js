// Vue.component('event', {

// })

let vm = new Vue({
    el: '#app',
    data: {
        events: null,
        citySearch: null,
    },
    methods: {
        getEvents: function() {
            axios({
                method: "get",
                params: {
                    apikey: 'ZAfftX5BnSjZ7ipPGzYzNZ7ObbVKzTh9',
                    city: this.citySearch,
                    stateCode: null,
                    keyword: 'music',
                },
                url: "https://app.ticketmaster.com/discovery/v2/events",
            }).then(response => this.events = response.data._embedded.events)
        },
        citySubmit: function() {
            this.getEvents();
        }
    },
    mounted: function() {
        console.log('test');
        this.getEvents();
    }
});