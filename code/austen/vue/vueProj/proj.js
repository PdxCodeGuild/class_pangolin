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
            info: []
        }
    },
    mounted () {
        axios({
            method: 'get',
            url:'https://app.ticketmaster.com/discovery/v2/events?apikey=ILjk0YWDkMs9CyCjpRCsSMqCs5P2vjGd&locale=*',
            async: true,
            // headers:{
            //     Authorization: 'Bearer 5BRHG6QOBATA4BU5K6'
            // }
        }).then(response=>(this.info=response),
        console.log(this.info))
    }
});