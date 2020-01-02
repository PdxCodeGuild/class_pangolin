var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

//make a border
ctx.strokeStyle = "magenta";
ctx.lineWidth = 15;
ctx.strokeRect(20, 20, 860, 560)

let ball = {
    radius: 30,
    px: Math.random()*835,
    py: Math.random()*535,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

function main_loop() {
    ctx.clearRect(25, 25, 850, 550);
    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    if (ball.px > 835 || ball.px < 35) {
        ball.vx = -ball.vx;
    }

    if (ball.py > 535 || ball.py < 35) {
        ball.vy = -ball.vy;
    }
  
    // draw the ball
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'magenta';
    ctx.fill();

    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);