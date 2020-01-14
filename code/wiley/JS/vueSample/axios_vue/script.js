Vue.component("todo-item", {
  props: ["todo"],
  template: `<li>{{ todo.text }}</li>`
});
Vue.component("thing", {
  template: `<ol><slot></slot></ol>`
});
new Vue({
  el: "#app",
  data: {
    groceryList: [
      { id: 0, text: "veggies" },
      { id: 1, text: "cheese" },
      { id: 2, text: "something else" }
    ]
  }
});
console.log("test");
// data (){
//     return {
//         info:null,
//         loading: true,
//         errored: false
//     }
// },
// filters: {
//     currencydecimal (value) {
//         return value.toFixed(2)
//     }
// },
// mounted () {
//     axios
//         .get('https://api.coindesk.com/v1/bpi/currentprice.json')
//         .then(response => (this.info = response.data.bpi))
//         .catch(error => {console.log(error)
//         this.errored = true
//     })
//         .finally(() => this.loading = false)
// }
