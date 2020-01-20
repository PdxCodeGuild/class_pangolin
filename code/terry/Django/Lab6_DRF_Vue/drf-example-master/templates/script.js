new Vue({
    el: '#app',
    data: {
        "first_name": "",
        "last_name": "",
        "cohort": "",
        "favorite_topic": "",
        "favorite_teacher": "",
        "capstone": ""
    },
    methods: {
        getRandomPerson: function() {
            axios({
                method: 'get',
                url: 'https://randomuser.me/api/',
                dataType: 'json',
            }).then(response => this.result = response.data.results);
        },
    },
    mounted: {
        axios({
            method: 'get',
            url: '/students/v1/v1/',
            dataType: 'json',
        }).then(response => this.result = response.data.results);
    }
});