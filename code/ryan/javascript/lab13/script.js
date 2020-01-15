let vm = new Vue({
    el: '#app',
    data: {
        word: null,
        searchWord: "",
        searchAuthor: "",
        quotes: null,
        thisType: ""
    },

    methods: {
        getQuotes: function() {
            axios({
                method: "get",
                url: 'https://favqs.com/api/quotes',
                headers: {
                    Authorization: 'Token token="1de4a15a706560aad25ab52cc75e4059"'
                },
                params: {
                    filter: this.word,
                    type: this.thisType
                }, 

            }).then(response => this.quotes = response.data.quotes)
        },
        checkWord: function() {
            document.getElementById('radio1').checked = true;
            document.getElementById('text2').value = "";
            this.searchAuthor = "";
            this.thisType = "tag";
            document.getElementById('text1').focus();
        },

        checkAuthor: function() {
            document.getElementById('radio2').checked = true;
            document.getElementById('text1').value = "";
            this.searchWord = "";
            this.thisType = "author";
            document.getElementById('text2').focus();
            // console.log(this.quotes);
        },
        checkClick: function() {
            if (this.searchAuthor === "" && this.searchWord === "") {
                this.word = null;
            }
            else if (document.getElementById('radio1').checked === true) {
                this.word = this.searchWord;
            } else {
                this.word = this.searchAuthor;
            }
            this.getQuotes();
        },
    },
    mounted: function() {
        console.log('works');
        this.getQuotes();
        },
});