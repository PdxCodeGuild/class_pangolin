let vm = new Vue({
    el: '#app', //element
    data: {     //model to store the state of the webpage
        exercises: [
            { id: 1, text: 'pushups', completed: false },
            { id: 2, text: 'pullups', completed: false },
            { id: 3, text: 'run', completed: false },
        ],
        newExerciseItem: {
            id: 4,
            text: "",
            completed: false,
            color: "#OF4C81"
        }
    },
    methods: {
        loadData: function() {      //loads data from localStorage
            window.localStorage.setItem('exercises', JSON.stringify(this.exercises))
        },
        addExercise: function () {
            this.exercises.push({
                id: this.newExerciseItem.id,
                text: this.newExerciseItem.text,
                completed: this.newExerciseItem.completed,
                color: this.newExerciseItem.color
            });
            this.newExerciseItem.id++;
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