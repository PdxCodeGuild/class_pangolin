/* ----- VUE ----
Vue is a MVVM framework.  (Model view, view model)
    Model <---> View Model <---> View
 (data/state) - (Vue Syncs) - (Template)

View model has a "shadow DOM"
-A shadow DOM is when VUE updates the view model, but doesn't re-render the template until it knows the fastest way to update. 

READ THE VIEW DOCS THEY ARE GOOD.
Vue uses components, as modular blocks of codes to apply when needed.  
*/

//COMPONENTS
//start by defining a new component
Vue.component('button-counter', {
    data: function(){ //the data in a compenent is a function
        return {
            count:0
        }
    },
    template: '<button v-on:click="count++"> You clicked me {{ count }} times. </button>' //the template is the html blue-print
});
//you can then call this into your HTML with a call like this:
<div id="components-demo">
        <button-counter></button-counter>
</div>
//then attach is to a new component in your script like this:
new Vue({ el: '#components-demo' });

//the element <slot> is used to add a value into a Vue element.  
// if you use a custom Vue element, you can then add <sloy></slot> for where you want it to be. 


//HOW TO USE VUE WITH AXIOS
/*
Make sure to loadboth axios and vue into your HTML, BEFORE you load your script
Build a Vue, and in the methods make a function that gets called on a command (button click listener).  This function will make a axios call. [get(params,url,method), then(the promise)].  With the data you parse and gather from the API, prduce information to the user on the HTML. 
wit VUE, the axios promise function is easy.  .then(res => this.results = res.data.apistuff)
IT IS IMPORTANT TO USE AN ARROW FUNCTION IN THE VUE/AXIOS COMBO.  The arrow function doesn't overwrite your this.vue stuff because of the scope of an arrow function compared to a full function.

*/