Vue.component('quotes', {
    data:function(){
        return{
        questionInput: '',
        info: []
        }
    },
    template: `
        <form class="form">
            <input class="input"v-model="questionInput" type= "text" placeholder="Type of Quote"></input>
            <button class="button"@click.prevent="getQuotes">Search</button>
        </form>
    `,
    methods:{
        getQuotes: function() {
            axios({
                method:"get",
                url:"https://favqs.com/api/quotes/",
                headers:{
                    Authorization: 'Token token="542c73b9613a3d9d98ddecbf1257594d"'
                },
                params: {
                    filter: this.questionInput,
                    type: 'tag',
                    // quotes: this.questionInput
                }
            })
            .then(response => {(this.info = response.data.quotes);
            console.log(this.info);
            this.$emit('results', this.info)
            })
        }
    }     
});
let vm = new Vue ({
    el:'#app',
    data: {
        info:[],
        qotd:null
    },
    mounted() {
        axios({
            url:'https://favqs.com/api/qotd',
            method: 'get',
        }).then(response => {(this.qotd = response.data.quote.body)})
    }
});