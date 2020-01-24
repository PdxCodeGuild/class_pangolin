new Vue({
    el: '#vue-app',
    data: {
        name: 'Casey',
        job: 'Customer Success Manager',
        website: 'http://www.mindenmusic.com',
        websiteTag: '<a href="http://www.mindenmusic.com">Minden Music</a>'
    },
    methods: {
        greet: function(time){
            return 'Good ' + time + ' ' + this.name;
        }
    }
});