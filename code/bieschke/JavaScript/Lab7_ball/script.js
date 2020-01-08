// canvas params
let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');
let width = 750;
let height = 750;
ctx.strokeStyle = 'blue';
ctx.strokeRect(0, 0, width, height);

balls = [];

let ball = {
    radius: Math.random() * 25,
    px: Math.random() * (width - 25),
    py: Math.random() * (height + 25),
    vx: (2 * Math.random()) * 10,
    vy: (2 * Math.random()) * 10
};

function createBall() {

    let ball = {
        radius: Math.random() * 25,
        px: Math.random() * (width - 25),
        py: Math.random() * (height + 25),
        vx: (2 * Math.random()) * 10,
        vy: (2 * Math.random()) * 10
    };
    balls.push(ball);
}
//draws the balls in the balls array
//once the array is populated, it is necessary to work with the indexes of each individual ball hereafter
function drawBall() {
    for (let i = 0; i < balls.length; ++i) {

        ctx.beginPath();
        ctx.arc(balls[i].px, balls[i].py, balls[i].radius, 0, 2 * Math.PI, false);
        ctx.closePath();
        //rainbow flashing
        //ctx.fillStyle = 'hsl(' + 360 * Math.random() + ', 50%, 50%)';
        ctx.fillStyle = 'red';
        ctx.fill();
    }
};

function clear() {
    ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
    ctx.fillRect(0, 0, width, height);
}

function mainLoop() {
    clear();
    drawBall();
    for (let i = 0; i < balls.length; ++i) {

        //a ball in motion stays in motion
        balls[i].px += balls[i].vx;
        balls[i].py += balls[i].vy;

        //unless it is acted upon by an outside param
        balls[i].vx *= .99;
        balls[i].vy += .25;

        //bouncing into boundaries
        if (balls[i].py + balls[i].vy > (height - balls[i].radius) || balls[i].py + balls[i].vy < balls[i].radius) {
            balls[i].vy = -balls[i].vy;
        };
        if (balls[i].px + balls[i].vx > (width - balls[i].radius) || balls[i].px + balls[i].vx < balls[i].radius) {
            balls[i].vx = -balls[i].vx;
        };
    }
    window.requestAnimationFrame(mainLoop);

}
window.requestAnimationFrame(mainLoop);

// moar clicks, moar balls
cnv.addEventListener('click', function (e) {
    createBall();
});