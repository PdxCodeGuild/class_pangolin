function timeFunction() {
    setTimeout(function() {
        alert("After 5 seconds!");
    }, 5000);
}
// Declare Variables
var canvas;
var ctx;
var ballX = 90;
var ballY = 90;
var xVelocity = 2;
var yVelocity = 2;
var color = '#ccff99';
var ballWidth = 25;

// Create canvas
window.onload = function() {
    canvas = document.getElementById('myCanvas');
    ctx = canvas.getContext('2d');
    setInterval(draw, 1000 / 60);
}

// Draw Everything
function draw() {

    // Create canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Create the ball
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.arc(ballX, ballY, ballWidth, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();

    // Change Ball Position
    ballX += xVelocity;
    ballY += yVelocity;

    // Bounce ball off left & change ball color
    if (ballX - ballWidth <= 0) {
        xVelocity = -xVelocity * 0.90;
        changeColor();
    }

    // Bounce ball off right & change ball color
    if (ballX + ballWidth >= canvas.width) {
        xVelocity = -xVelocity * 0.90;
        changeColor();
    }

    // Bounce ball off top & change ball color
    if (ballY - ballWidth <= 0) {
        yVelocity = -yVelocity + 1.5;
        changeColor();
    }

    // Bounce ball off bottom & change ball color
    if (ballY + ballWidth >= canvas.height) {
        yVelocity = -yVelocity * 0.95;
        changeColor();
    }

}

function changeColor() {

    var x = Math.random() * 10;
    var n = Math.ceil(x);
    var nu = n;

    if (nu == 1) {
        color = '#ffaacc'
    }
    if (nu == 2) {
        color = 'orange'
    }
    if (nu == 3) {
        color = 'teal'
    }
    if (nu == 4) {
        color = 'turquoise'
    }
    if (nu == 5) {
        color = 'purple'
    }
    if (nu == 6) {
        color = 'lightgreen'
    }
    if (nu == 7) {
        color = 'skyblue'
    }
    if (nu == 8) {
        color = 'darkgrey'
    }
    if (nu == 9) {
        color = 'crimson'
    }
    if (nu == 10) {
        color = 'pink'
    }
}

function game_loop() {
    window.requestAnimationFrame(game_loop);
    update(1.0);
    draw();
}
window.requestAnimationFrame(game_loop);