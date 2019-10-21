let app = new Vue({
  el: '#app',
  data: {
      message: 'Hello world!',
      myboolean: true,
      mynum: 0,
      todos: [
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ]
  },
  methods: {
    buttonHandler: function() {
      this.todos.push(this.todos.shift())
    }
  }
})