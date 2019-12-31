// define canvas context
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

// draw border
ctx.strokeStyle = "#00FFCC";
ctx.lineWidth = 15;
ctx.strokeRect(20, 20, 860, 560);

// define ball object
let ball = {
    radius: 30,
    px: Math.random()*845,
    py: Math.random()*545,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

// create loop that moves ball 
function main_loop() {
    // clearRect
    ctx.clearRect(25, 25, 850, 550);
    
    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    // check if it hit boundary
    if (ball.px > 850 || ball.px < 50) {
        ball.vx = -ball.vx;
    }

    if (ball.py > 550 || ball.py < 50) {
        ball.vy = -ball.vy;
    }
    
    // draw ball
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = "#00FFCC";
    ctx.fill();
    window.requestAnimationFrame(main_loop);
}

window.requestAnimationFrame(main_loop);