let draggable = document.getElementById("draggable");
let mouseButtonDown = false;

draggable.addEventListener('mousedown', function(){
    mouseButtonDown = true;
    console.log("mousedown")
});
draggable.addEventListener('mouseup', function(){
    mouseButtonDown = false;
    console.log("mouseup")
});
draggable.addEventListener('mouseleave', function(){
    mouseButtonDown = false;
    console.log("mouseleave")
});
draggable.addEventListener('mousemove', function(event){
    console.log("mousemove")
    if(mouseButtonDown){
        this.style.top = `${event.pageY - 100}px`;   // to base off center
        this.style.left = `${event.pageX - 100}px`;  // to base off center
    }
});