let width = 500;
let height = 500;
let c = document.getElementById('myCanvas');
let ctx = c.getContext('2d');
let start;

let ball = {
    radius: 20,
    px: Math.random() * width,
    py: Math.random() * height,
    vx: (2 * Math.random() - 1) * 10,
    vy: (2 * Math.random() - 1) * 10,

    draw: function() {
        ctx.beginPath();
        ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = 'green';
        ctx.fill();
    }
};

function draw() {
    ctx.clearRect(0, 0, c.width, c.height);
    ball.draw();
    ball.x += ball.vx;
    ball.y += ball.yx;

    window.requestAnimationFrame(draw);
}
window.requestAnimationFrame(draw);

c.addEventListener('click', function(e) {
    start = window.requestAnimationFrame(draw);
});