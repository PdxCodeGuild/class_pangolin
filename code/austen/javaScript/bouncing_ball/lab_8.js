let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

let balls = [];
for (let i=0; i<50; ++i){
    let ball = {
        //ball radius
        radius: 20,
        px: Math.random()*cnv.width-25,
        py: Math.random()*cnv.height+25,
        vx: (2*Math.random()-1)*30,
        vy: (2*Math.random()-1)*30,
    };
    balls.push(ball);
};

function draw(){
    
    ctx.fillStyle = 'black';
    
    for (var i=0; i<balls.length; ++i) {
        var ball = balls[i];

        ctx.beginPath();
        ctx.arc(ball.px, ball.py, ball.radius, 0, Math.PI * 2, true);
        ctx.fill();
    }
}



function clear(){
    ctx.fillStyle = 'rgba(173, 216, 255, 0.3)';
    ctx.fillRect(0, 0, cnv.width, cnv.height);
}

function game(){
    clear();
    // ball.draw();
    for (let i=0; i<balls.length; ++i){
        let ball = balls[i]
    //sets it in motion
        ball.px += ball.vx;
        ball.py += ball.vy;
        ball.vy *= .99;
        ball.vy += .5;
        
    //this checks if it is bouncing aginst the y axis
        if (ball.py + ball.vy > cnv.height-25 || ball.py + ball.vy < 25){
            ball.vy = -ball.vy;
            //this line is friction
            ball.vy *= .99;
            ball.vx *= .99;
        }
    //this checks if it is bouncing aginst the x axis
        if (ball.px + ball.vx > cnv.width-25 || ball.px + ball.vx < 25){
            ball.vx = -ball.vx;
            //this line is friction
            ball.vy *= .99;
            ball.vx *= .99;
        }
    }
}
function game_loop() {
    window.requestAnimationFrame(game_loop);
    game();
    draw();
}


cnv.addEventListener('click', function(e){
    window.requestAnimationFrame(game_loop);
    
});
