Vue.component('information', {
    props: ['info'],
    data: function() {
        return {
            id: 1,
            text: "",
        }
    },
    // this template tells the info from the api how to display to the screen on the left
    template: `
        <div class="container-left">
            <p>Name: {{ info.name }}</p>
            <p>Duration of Effect: {{ info.duration }}</p>
            <p>Casting Time: {{ info.casting_time }}</p>
            <p>Spell Level: {{ info.level }}</p>
            <p>School of Magic: {{ info.school.name }}</p>
            <p>Materials Needed: {{ info.material }}</p>
            <p>Components Needed: {{ info.components }}</p>
            <p>Class of Use: <span v-for="spell_class in info.classes">{{ spell_class.name }}, </span></p>
            <p>Spell Range: {{ info.range }}</p>
            <p>Page number in Core Rule Book: {{ info.page }}</p>
            <p>Description of Spell: {{ info.desc }}</p>
            <button @click="moveToList()">Add</button>
            ${/* <p v-if="info.higher_level != 0">What happens at Higher Levels: {{ info.higher_level[0] }}</p> */''}
        </div>
    `,
    methods: {
    itemSelected: function() {
        this.$emit('itemSelected', {id:this.id, text:this.text});
        this.id++
    },
    moveToList: function() {
        this.$emit('move-to-list', this.info);
        this.id++
    },
}
});

Vue.component('favorites', {
    props: ['info-list'],
    data: function() {
        return {
            id: 1,
            text: "",
        }
    },
    // this moves the added spell to the list of the right and tells it how to display in that list
    template: `
        <div class="container-right">
            <div v-for="info in infoList" :key="info._id">
                <p><b>Name: {{ info.name }}</b></p>
                <p>Duration of Effect: {{ info.duration }}</p>
                <p>Casting Time: {{ info.casting_time }}</p>
                <p>Spell Level: {{ info.level }}</p>
                <p>School of Magic: {{ info.school.name }}</p>
                <p>Materials Needed: {{ info.material }}</p>
                <p>Components Needed: {{ info.components }}</p>
                <p>Class of Use: <span v-for="spell_class in info.classes">{{ spell_class.name }}, </span></p>
                <p>Spell Range: {{ info.range }}</p>
                <p>Page number in Core Rule Book: {{ info.page }}</p>
                <p>Description of Spell: {{ info.desc }}</p>
                ${/* <p v-if="info.higher_level != 0">What happens at Higher Levels: {{ info.higher_level[0] }}</p> */''}
            </div>
        </div>
    `,
    methods: {
    moveToList: function() {
        this.$emit('moveToList', {id:this.id, text:this.text});
        this.id++
    },
}
});

let vm = new Vue ({
    el: '#data',
    data: {
        options: ["spells"],
        selected: '',
        items: [],
        selectedOption: '',
        result: {},
        favorites: [],
        },
    methods: {
        getSpells: function() {
            // this retrieves the spell from the api
            this.items = [];
            let key = 'name';
            if(this.selectedOption === 'spells') key = 'name';

            fetch("http://www.dnd5eapi.co/api/" + this.selectedOption)
            .then(res=>res.json())
            .then(res=> {
                // "fix" the data to and set a label for all types
                this.items = res.results.map((item) => {
                    item.label = item[key];
                    console.log(item)
                    return item;
                }); 
            });
        },
        // this is the esecond drop down menu that is populated with the list of spells in alphabetical order
        itemSelected: function() {
            console.log(this.selected)
            axios ({
                method: "get", 
                baseURL:"http://www.dnd5eapi.co/api/",
                url: "/spells/" + this.selected,

            }).then(res=> this.result = res.data)
        },
        // this moves the chosen spell to the list on the right that keeps a running list of all spells added to favorites 
        moveToList: function(item) {
            this.favorites.push(item)
        }
    }
})