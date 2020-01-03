var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var x = canvas.width;
var y = canvas.height;
var vx = (2*Math.random()-1)*10
var vy = (2*Math.random()-1)*10;

function drawRect() {
    ctx.beginPath();
    ctx.rect(x, y, 10, 45, 120);
    ctx.stroke();
    ctx.fillStyle = "#b6af00";
    ctx.fill();
    ctx.closePath();
}

function draw() {

    ctx.canvas.width = window.innerWidth;
    ctx.canvas.height = window.innerHeight;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawRect();
    
    if(x + vx > canvas.width || x + vx < 0) {
        vx = -vx + 3;
    }
    if(y + vy > canvas.height || y + vy < 0) {
        vy = -vy * .12;
    }
    
    x += vx;
    y += vy;
}

setInterval(draw, 1);