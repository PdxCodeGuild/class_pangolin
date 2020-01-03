let width = 500;
let height = 500;
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
let start;

var my_gradient = ctx.createLinearGradient(0, 0, 170, 0);
my_gradient.addColorStop(0, "black");
my_gradient.addColorStop(1, "white");
ctx.fillStyle = my_gradient;
ctx.fillRect(0, 0, canvas.width, canvas.height);


let ball = {
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (2 * Math.random() - 1) * 10,
    vy: (2 * Math.random() - 1) * 10,
    radius: 20,
    draw: function() {
        my_gradient.addColorStop(0, "lightgreen");
        my_gradient.addColorStop(1, "white");
        ctx.fillStyle = my_gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.rect(0, 0, canvas.width, canvas.height);
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
        ctx.closePath();
        ctx.fillStyle = 'green';
        ctx.fill();

    }
};

function draw() {

    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ball.draw();

    ball.vy *= .99;
    ball.vy += .25;

    ball.x += ball.vx;
    ball.y += ball.vy;

    if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
        ball.vy = -ball.vy;
    }
    if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
        ball.vx = -ball.vx;
    }
    start = window.requestAnimationFrame(draw);
}

canvas.addEventListener('mouseover', function(e) {
    start = window.requestAnimationFrame(draw);
});

canvas.addEventListener('mouseout', function(e) {
    window.cancelAnimationFrame(start);
});

ball.draw();