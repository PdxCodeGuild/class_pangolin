Vue.component('rand-ex', {
    template: `<div v-on:click.prevent="$emit('rand-ex')" class='btn'>Give me something to do right now!</div>`
})

Vue.component('arms-button', {
    template: `<div v-on:click.prevent="$emit('arms-button')" class='btn'>Give me an arm exercise!</div>`
})

Vue.component('search-button', {
    template: `<div v-on:click.prevent="$emit('search-button')" class='btn'>Search</div>`
})

Vue.component('search-button2', {
    template: `<div v-on:click.prevent="$emit('search-button2')" class='btn'>GO!</div>`
})

Vue.component('clear', {
    template: `<div v-on:click="$emit('clear')" class='btn'>clear results</div>`
})

let vm = new Vue({
    el: "#app",
    data: {
        workout: {
            name: null,
            description: null,
        },
        database: [],
    },

    methods: {
        // gets a random exercise in english
        randEx: function () {
            axios({
                method: 'GET',
                url: "https://wger.de/api/v2/exercise",
                params: {
                    status: 2,
                    language: 2,
                    limit: 100
                },
                headers: {
                    Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6'
                }
            }).then(response => {
                let english = response.data.results.filter(function (item) {
                    return item.name;    //sorts named responses in english
                });
                console.log(english)
                let pick = Math.floor(Math.random() * english.length);
                this.workout.name = english[pick].name
                this.workout.description = english[pick].description
            }).catch(error => console.log(error))
        },
        // gets a random arm exercise
        armsButton: function () {
            axios({
                method: 'GET',
                url: "https://wger.de/api/v2/exercise",
                params: {
                    status: 2,
                    language: 2,
                    limit: 200,
                    // name: 'Arms'
                },
                headers: {
                    Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6'
                }
            }).then(response => {
                let arms = response.data.results
                let bacon = Math.floor(Math.random() * arms.length);
                this.workout.name = arms[bacon].name
                this.workout.description = arms[bacon].description
            }).catch(error => console.log(error))
        },
        //lets the user search for one exercise
        searchButton: function () {
            axios({
                method: 'GET',
                params: {
                    language: 2,
                    status: 2,
                    name: this.input,
                    limit: 200
                },
                url: "https://wger.de/api/v2/exercise",

                headers: {
                    Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6'
                }
            }).then(response => {
                let usr = response.data.results
                let muscle = Math.floor(Math.random() * usr.length);
                this.workout.name = usr[muscle].name,
                this.workout.description = usr[muscle].description
            }).catch(error => console.log(error))

        },
        //displays all exercises with the desired criteria
        searchButton2: function () {
            axios({
                method: 'GET',
                params: {
                    language: 2,
                    status: 2,
                    name: this.input,
                    limit: 200
                },
                url: `https://wger.de/api/v2/exercise`,
                headers: {
                    Authorization: 'Token 274dce7a2317a21098a9358b43d837fa310ccea6'
                }
            }).then(response => {
                this.database = response.data.results
                console.log(this.database)
            }).catch(error => console.log(error))
        },
        clear: function () {
            this.database = []
            this.workout = {
                name: null,
                description: null
            }
        }

    }
})