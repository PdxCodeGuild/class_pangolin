// canvas params
let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');
let width = 1000;
let height = 1000;
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
};

function mainLoop() {
  clear();
  drawBall();
  for (let i = 0; i < balls.length; ++i) {

    //a ball in motion stays in motion
    balls[i].px += balls[i].vx;
    balls[i].py += balls[i].vy;

    //bouncing into boundaries
    if (balls[i].py + balls[i].vy > (height - balls[i].radius) || balls[i].py + balls[i].vy < balls[i].radius) {
      balls[i].vy = -balls[i].vy;
      balls[i].vy *= .99;   //unless it is acted upon by an outside param
    };
    if (balls[i].px + balls[i].vx > (width - balls[i].radius) || balls[i].px + balls[i].vx < balls[i].radius) {
      balls[i].vx = -balls[i].vx;
      balls[i].vx *= .99;   //unless it is acted upon by an outside param
    };

    //bouncing into each other
    for (let i = 0; i < balls.length; ++i) {
      for (let j = 0; j < balls.length; ++j) {
        if (i !== j) {

          let distance = Math.sqrt(((balls[i].px - balls[j].px)**2) + ((balls[i].py - balls[j].py)**2))
          
          // console.log(distance)
          if (distance < (balls[i].radius + balls[j].radius))   //balls have collided
          {

            balls[i].vx = (balls[i].vx * (balls[i].radius - balls[j].radius) + (2 * balls[j].radius * balls[j].vx)) / (balls[i].radius + balls[j].radius);
            balls[i].vy = (balls[i].vy * (balls[i].radius - balls[j].radius) + (2 * balls[j].radius * balls[j].vy)) / (balls[i].radius + balls[j].radius);
            balls[j].vx = (balls[j].vx * (balls[j].radius - balls[i].radius) + (2 * balls[i].radius * balls[i].vx)) / (balls[i].radius + balls[j].radius);
            balls[j].vy = (balls[j].vy * (balls[j].radius - balls[i].radius) + (2 * balls[i].radius * balls[i].vy)) / (balls[i].radius + balls[j].radius);
            console.log('balls have collided')
          };
        };
      };
    };
  };
  window.requestAnimationFrame(mainLoop);

}
window.requestAnimationFrame(mainLoop);

// moar clicks, moar balls
cnv.addEventListener('click', function (e) {
  createBall();
});