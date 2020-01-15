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
            event: []
        }
    },
    methods:{
        getTickets: function () {
            axios({
                method: "get",
                url: "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=&dmaId=362&apikey=ILjk0YWDkMs9CyCjpRCsSMqCs5P2vjGd",
                async:true
            })
            .then(response => {this.event = response.data._embedded.events})
            this.$emit('newResults', this.event)
        },
        mounted: function() {
            console.log("It loaded!");
        },
        clearEvents: function(){
            this.event= []
            this.info= []
            }
        }
});