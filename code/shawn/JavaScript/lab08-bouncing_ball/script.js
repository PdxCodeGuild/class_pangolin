class Sphere {
    constructor(c, r, d) {
        // characteristics
        this.color = c;
        this.radius = r;
        this.density = d;
        this.volume = (4 / 3) * (Math.PI) * ((this.radius) ** 3);
        this.mass = this.density * this.volume;

        //position
        this.px = Math.random() * width;
        this.py = Math.random() * height;
        this.vx = (2 * Math.random() - 1) * 10;
        this.vy = (2 * Math.random() - 1) * 10;
    }
}


// get DOM elements
let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

// some variables 
let width = window.innerWidth - 10;
let height = window.innerHeight - 10;
let friction = .9;

// setup canvas
canvas.setAttribute("width", width);
canvas.setAttribute("height", height);

// let ballGreen = new Sphere("green", 40, 1.0);
// let ballRed = new Sphere("red", 40, 1.0);
// let ballBlue = new Sphere("blue", 40, 1.0);
// let balls = [ballGreen, ballRed, ballBlue];
let balls = [];

for (let i = 0; i < 100; i++) {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);

    balls.push(new Sphere(`rgb(${r},${g},${b})`, 10, 1.0));
}


for (let ball of balls) {
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = ball.color;
    ctx.fill();
}

function drawBall(ball) {
    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    // gravity
    // ball.vy += .5;

    // check if it hit a boundary
    if (ball.px - ball.radius < 0) {
        ball.vx *= -1 * friction;
        ball.px = ball.radius;
    } else if (ball.px + ball.radius > width) {
        ball.vx *= -1 * friction;
        ball.px = width - ball.radius;
    } else if (ball.py - ball.radius < 0) {
        ball.vy *= -1 * friction;
        ball.py = ball.radius;
    } else if (ball.py + ball.radius > height) {
        ball.vy *= -1 * friction;
        ball.py = height - ball.radius;
    }

    // draw the ball
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = ball.color;
    ctx.fill();
}

function checkCollisions(firstBall) {
    // first conduct AABB check
    for (let secondBall of balls) {
        // only look at balls that aren't the current ball
        if (firstBall != secondBall) {

            // axis-aligned bounding box
            if (firstBall.px + firstBall.radius + secondBall.radius > secondBall.px
                && firstBall.px < secondBall.px + firstBall.radius + secondBall.radius
                && firstBall.py + firstBall.radius + secondBall.radius > secondBall.py
                && firstBall.py < secondBall.py + firstBall.radius + secondBall.radius) {
                let distance = Math.sqrt((firstBall.px - secondBall.px) ** 2 + (firstBall.py - secondBall.py) ** 2);
                if (distance < firstBall.radius + secondBall.radius) {
                    // console.log(`${firstBall.color} collides with ${secondBall.color}`)
                    // calculate changes in velocity
                    let newVelX1 = (firstBall.vx * (firstBall.mass - secondBall.mass) + (2 * secondBall.mass * secondBall.vx)) / (firstBall.mass + secondBall.mass);
                    let newVelY1 = (firstBall.vy * (firstBall.mass - secondBall.mass) + (2 * secondBall.mass * secondBall.vy)) / (firstBall.mass + secondBall.mass);
                    let newVelX2 = (secondBall.vx * (secondBall.mass - firstBall.mass) + (2 * firstBall.mass * firstBall.vx)) / (firstBall.mass + secondBall.mass);
                    let newVelY2 = (secondBall.vy * (secondBall.mass - firstBall.mass) + (2 * firstBall.mass * firstBall.vy)) / (firstBall.mass + secondBall.mass);

                    // apply changes in velocity
                    firstBall.vx = newVelX1;
                    firstBall.vy = newVelY1;
                    secondBall.vx = newVelX2;
                    secondBall.vy = newVelY2;

                    firstBall.px += newVelX1;
                    firstBall.py += newVelY1;
                    secondBall.px += newVelX2;
                    secondBall.py += newVelY2;

                }
            }
        }
    }
}

function main_loop() {

    // clear the canvas
    ctx.clearRect(0, 0, width, height);

    // draw each ball's location
    for (let ball of balls) {
        drawBall(ball);
    }

    // check for collisions
    for (let ball of balls) {
        checkCollisions(ball);
    }

    window.requestAnimationFrame(main_loop);
}

function reportWindowSize() {
    height = window.innerHeight - 10;
    width = window.innerWidth - 10;
    canvas.setAttribute("width", width);
    canvas.setAttribute("height", height);
}

window.onresize = reportWindowSize;

window.requestAnimationFrame(main_loop);