let draggable = document.getElementById("draggable");

let mouseButtonDown = false;

document.body.addEventListener('mousedown', function() {
    mouseButtonDown = true;
});

document.body.addEventListener('mouseup', function() {
    mouseButtonDown = false;
});

document.body.addEventListener('mouseleave', function() {
    mouseButtonDown = false;
});

draggable.body.addEventListener('mousemove', function(event) {
    console.log(event.pageX, event.pageY)
    if (mouseButtonDown) {
        this.style.top = `${event.clientY - 100}px`;
        this.style.left = `${event.clientX - 100}px`;
    }
});