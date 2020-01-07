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
