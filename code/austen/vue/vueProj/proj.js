Vue.component('activity',{
    data: function(){
        return {
            answer:'',
            info:[]
            }
        },
        template: `
        <form>
            <select id="activitySel" v-model="answer">
                <option value="" seclected disabled>Please Choose One...</option>
                <option value="education">Education</option>
                <option value="social">Social</option>
                <option value="diy">DIY</option>
                <option value="recreational">Recreational</option>
                <option value="charity">Charity</option>
                <option value="music">Music</option>
            </select>
            <button class="find" @click.prevent="findActivity">Find</button>
        </form>
        `,
        methods: {
            findActivity: function(){
                axios({
                    method: "get",
                    url: "https://www.boredapi.com/api/activity/",
                    params: {
                        filter: this.answer,
                        type: this.answer
                    }
                })
                .then(response => {(this.info = response.data);
                parseFloat(this.info.price),
                console.log(this.info);
                console.log(this.info.price);
                this.$emit('results', this.info)

            })
                    
        }
    }
});

let vm = new Vue ({
    el:'#app',
    data: function() {
        return {
            info: [],
            event: ''
        }
    },
    methods:{
        getData: function() {
            let token= "SMGqCoSLZO-CnmSN28MitIBPHTxQhaxcQmd7nFWURV6NKSu_xJwkPylSSfPJfcoafykRCg51GCNUA1m_fEeJej5uT0wfQZJMaZKRd1R2nY-jsRlNVt0MEcQyMGIaXnYx"
            axios({
                method: 'get',
                url:'https://api.yelp.com/v3/events/featured',
                headers:{
                    'Authorization': 'Bearer'+ SMGqCoSLZO-CnmSN28MitIBPHTxQhaxcQmd7nFWURV6NKSu_xJwkPylSSfPJfcoafykRCg51GCNUA1m_fEeJej5uT0wfQZJMaZKRd1R2nY-jsRlNVt0MEcQyMGIaXnYx 
                }, 
            }).then(response=>(console.log(response),this.info=response),
            console.log(this.info))
        },
        getStuff: function() {
            axios({
                method: "get",
                url: "https://www.boredapi.com/api/activity/",
            })
            .then(response => {(this.info = response.data);
            parseFloat(this.info.price),
            console.log(this.info);
            console.log(this.info.price);

        })
        },
        getTickets: function () {
            axios({
                method: "get",
                url: "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=&dmaId=362&apikey=ILjk0YWDkMs9CyCjpRCsSMqCs5P2vjGd",
                // params: {
                //     filter: this.event.events
                // },
                async:true
            })
            .then(response => {this.event = response.data._embedded.events})
            this.$emit('newResults', this.event)
        },
        mounted: function() {
            console.log("It loaded!");
         }
    }
});