const NYTBaseUrl = "https://api.nytimes.com/svc/topstories/v2/";
const ApiKey = "11MjPRexeQJ64gLOIbTSjJCGqgeJtTio";
// const ApiKey = config.KEY;
const SECTIONS = "home, arts, books, food, movies, science, theater, travel, upshot";

function buildUrl(url) {
    return NYTBaseUrl + url + ".json?api-key=" + ApiKey;
}

// Pass info to browser
Vue.component('news-list', {
    props: ['results'],
    template: `
    <section>
      <div class="row" v-for="posts in processedPosts">
        <div class="columns large-3 medium-6" v-for="post in posts">
          <div class="card">
            <div class="card-divider">
            {{ post.title }}
            </div>
            <a :href="post.url" target="_blank"><img :src="post.image_url"></a>
            <div class="card-section">
              <p>{{ post.abstract }}</p>
            </div>
          </div>
        </div>
      </div>
  </section>
  `,
    computed: {
        processedPosts() {
            let posts = this.results;

            // Loop through API results, search multimedia array of each result; find 
            // correct media type and format. Add image_url attribute
            // If n/a, use default placeholder image.
            posts.map(post => {
                let imgObj = post.multimedia.find(media => media.format === "superJumbo");
                post.image_url = imgObj ? imgObj.url : "http://placehold.it/300x200?text=N/A";
            });

            // Put Array into Chunks
            let i, j, chunkedArray = [],
                chunk = 4;
            for (i = 0, j = 0; i < posts.length; i += chunk, j++) {
                chunkedArray[j] = posts.slice(i, i + chunk);
            }
            return chunkedArray;
        }
    }
});

const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        sections: SECTIONS.split(', '), // create an array of the sections
        section: 'science', // set default section to 'science'
        // loading: true,
        // title: ''
    },
    mounted() {
        this.getPosts('science');
    },
    methods: {
        getPosts(section) {
            let url = buildUrl(section);
            axios.get(url).then((response) => {
                this.loading = false;
                this.results = response.data.results;
                let title = this.section !== 'home' ? "Top stories in '" + this.section + "' today" : "Top stories today";
                this.title = title + "(" + response.data.num_results + ")";
            }).catch((error) => {
                console.log(error);
            });
        }
    }
});