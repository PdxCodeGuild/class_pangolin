Vue.component('add-item', {
    data: function () {
        return {
            id: 1,
            text: "",
            completed: false,
            color: "#000000"
        }
    },
    template: `
    <form>
            <input type="text" placeholder="new exercise" v-model="text" />
            <input type="color" v-model="color" />
            <button v-on:click.prevent="add">Add</button>   
            <!-- .prevent automatically prevents the default refresh action of form -->
            <button v-on:click.prevent="deleteCompleted">Delete Completed</button>
            <button v-on:click.prevent="completeAll">Complete All</button>
            <slot></slot>
    </form>
    `,
    methods: {
        add: function () {
            this.$emit('add', { id: this.id, text: this.text, completed: this.completed, color: this.color })
            this.id++
        }
    }
});

Vue.component('exercise-item', {
    props: ['exercise'],
    template: `
    <li>
     <p
        v-bind:class="{completed: exercise.completed}" 
        v-bind:style="{color: exercise.color}"
        >
        {{exercise.text}}
        </p>

        <input type="checkbox" v-model="exercise.completed"/>
        <input type="color" v-model="exercise.color" />
        <button v-on:click.prevent="$emit('delete-exercise', exercise)">Delete</button>
    </li>
    `,
    methods: {
        // deleteExercise: function (exerciseItem) {
        //     // this.exercises.splice(exerciseIndex, 1);
        //     this.$parent.exercises.splice(this.exercises.indexOf(exerciseItem), 1);

        // }
    },
});

let vm = new Vue({
    el: '#app', //element
    data: {     //model to store the state of the webpage
        exercises: [
            { id: 1, text: 'pushups', completed: false },
            { id: 2, text: 'pullups', completed: false },
            { id: 3, text: 'run', completed: false },
        ],

    },
    methods: {
        loadData: function () {      //loads data from localStorage
            window.localStorage.setItem('exercises', JSON.stringify(this.exercises))
        },
        addExercise: function (newExerciseItem) {
            this.exercises.push(newExerciseItem);
        },
        deleteExercise: function (exerciseItem) {
            // this.exercises.splice(exerciseIndex, 1);
            this.exercises.splice(this.exercises.indexOf(exerciseItem), 1);
        },
        completeAll: function () {
            for (exercise of this.exercises) {
                exercise.completed = true;
            }
        },
        deleteCompleted: function () {
            let toBeCleared = this.exercises.filter(item => item.completed);
            for (exercise of toBeCleared) {
                this.deleteExercise(exercise)
            }
        }
    },
    computed: {
        completedItems: function () {
            return this.exercises.filter(item => item.completed);
        },
        incompletedItems: function () {
            return this.exercises.filter(item => !item.completed);
        }
    },
    mounted: function () {
        window.addEventListener('unload', this.loadData)
        const exerciseString = window.localStorage.getItem('exercises')
        console.log(exerciseString)
        console.log(exerciseString === 'undefined')

        if (exerciseString !== 'undefined') {
            console.log('truthy');
            this.exercises = JSON.parse(exerciseString);
        } else {
            console.log('falsy');
        }
    },

    beforeDestroy: function () {
        window.removeEventListener('unload', this.loadData)
    }
});