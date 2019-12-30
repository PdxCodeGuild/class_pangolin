var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d');
var raf;
var running = false;

var ball = {
    x:100,
    y:100,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    radius:25,
    color: 'green',
    draw: function() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI, true);
        ctx.closePath();
        ctx.fillStyle = this.color;
        ctx.fill();
    }
};
function clear() {
    ctx.fillStyle='rgba(255,255,245,0.3)';
    ctx.fillRect(0,0, canvas.width, canvas.height);
    
}
function draw() {
    clear();
    ball.draw();
    ball.x +=ball.vx;
    ball.y +=ball.vy;
    ball.vy += .7;
    if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
        ball.vy = -ball.vy;
        ball.vy *= .9;
        ball.vx *= .9;
        ball.color = `rgb(${ranCol()},${ranCol()},${ranCol()})`;
        console.log(ball.color);
        
;


    }
    if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
        ball.vx = -ball.vx;
        ball.vx *= .9;
        ball.vy *= .9;
        ball.color = `rgb(${ranCol()},${ranCol()},${ranCol()})`;
        console.log(ball.color);
    }
    raf = window.requestAnimationFrame(draw);

}
canvas.addEventListener('click',function(e) {
    if (!running) {
        raf = window.requestAnimationFrame(draw);
        running = true;
    }
});
canvas.addEventListener('mouseout', function(e) {
    window.cancelAnimationFrame(raf);
    running = false;
});

ball.draw();
console.log(Math.floor(Math.random()*255))
function ranCol() {
    return Math.floor(Math.random()*255)
}