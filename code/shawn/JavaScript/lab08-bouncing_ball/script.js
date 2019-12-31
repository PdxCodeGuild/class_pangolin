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
let ballQtyNum = document.getElementById("num-of-balls");
let frictionSlider = document.getElementById("friction-slider");
let agitateButton = document.getElementById("agitate");
let frictionAmount = document.getElementById("frictionAmount");
let gravityAmount = document.getElementById("gravityAmount");


// some variables 
let ballCount = ballQtyNum.value;
let maxBallSize = 50;
let minBallSize = 20;
let width = window.innerWidth - 10;
let height = window.innerHeight - 10;
let friction = frictionAmount.value;
let gravity = gravityAmount.value;

// setup canvas
canvas.setAttribute("width", width);
canvas.setAttribute("height", height);

let balls = [];

for (let i = 0; i < ballCount; i++) {
    // randomize colors
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);

    // randomize size, up to 100
    let size = Math.floor(Math.random() * maxBallSize) + minBallSize;

    // create new Sphere
    balls.push(new Sphere(`rgb(${r},${g},${b})`, size, 1.0));
}


for (let ball of balls) {
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = ball.color;
    ctx.fill();
}

function drawBall(ball) {

    // // physics
    // let Cd = 0.47;       // coefficient of drag, influenced by shape of object
    // let rho = 1.22;      // fluid density that ball is in
    // let ag = 9.81;       // connect to input gravity
    // let A = Math.PI * ball.radius * ball.radius / (10000);
    // let Fx = -0.5 * Cd * A * rho * ball.vx * ball.vx * ball.vx / Math.abs(ball.vx);
    // let Fy = -0.5 * Cd * A * rho * ball.vy * ball.vy * ball.vxy / Math.abs(ball.vy);

    // Fx = (isNaN(Fx) ? 0 : Fx)
    // Fy = (isNaN(Fy) ? 0 : Fy)

    // // calculate acceleration (F=ma)
    // let ax = Fx / ball.mass;
    // let ay = ag + (Fy / ball.mass);

    // // integrate to get velocity (using framerate as time)
    // ball.vx += ax*frameRate;  // where to get framerate?
    // ball.vy += ay*frameRate;  // where to get framerate? 

    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    // gravity
    ball.vy += parseFloat(gravity);

    // check if it hit a boundary
    if (ball.px - ball.radius < 0) {
        ball.vx *= -1 * (1 - friction);
        ball.px = ball.radius;
    } else if (ball.px + ball.radius > width) {
        ball.vx *= -1 * (1 - friction);
        ball.px = width - ball.radius;
    } else if (ball.py - ball.radius < 0) {
        ball.vy *= -1 * (1 - friction);
        ball.py = ball.radius;
    } else if (ball.py + ball.radius > height) {
        ball.vy *= -1 * (1 - friction);
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

    // for debug, print out some variables:
    // console.log(`gravity: ${gravity} friction: ${friction}`)


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

// event listeners
ballQtyNum.addEventListener("input", function () {
    let diff = ballQtyNum.value - ballCount;
    console.log(`diff is ${diff}`)
    if (diff < 0) {
        for (let i = 0; i < Math.abs(diff); i++) {
            balls.pop();
        }
    } else {
        for (let i = 0; i < diff; i++) {
            // randomize colors
            let r = Math.floor(Math.random() * 256);
            let g = Math.floor(Math.random() * 256);
            let b = Math.floor(Math.random() * 256);

            // randomize size, up to 100
            let size = Math.floor(Math.random() * maxBallSize) + minBallSize;

            // create new Sphere
            balls.push(new Sphere(`rgb(${r},${g},${b})`, size, 1.0));
        }
    }

    ballCount = ballQtyNum.value;

});
frictionAmount.addEventListener("input", function () {
    friction = frictionAmount.value;
})
gravityAmount.addEventListener("input", function () {
    gravity = gravityAmount.value;
})
agitateButton.addEventListener("click", function () {
    for (let ball of balls) {
        ball.vx = (2 * Math.random() - 1) * 50;
        ball.vy = (2 * Math.random() - 1) * 50;
    }
})
window.onresize = reportWindowSize;

window.requestAnimationFrame(main_loop);
