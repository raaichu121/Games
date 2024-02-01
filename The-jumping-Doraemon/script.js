score = 0;
cross = true;

audio = new Audio('background.mp3');
audio.loop = true;
const audiogo= new Audio('gameover.mp3');
setTimeout(()=>{
    audio.play();
},1000);

let gameIsOver = false;

document.onkeydown = function (e) {
    console.log("Key code is: ", e.key)
    if (!gameIsOver) {
        if (e.key == 'ArrowUp') {
            dore = document.querySelector('.dore');
            dore.classList.add('animateDore');
            setTimeout(() => {
                dore.classList.remove('animateDore')
            }, 700);
        }
        if (e.key == 'ArrowRight') {
            dore = document.querySelector('.dore');
            doreX = parseInt(window.getComputedStyle(dore, null).getPropertyValue('left'));
            dore.style.left = doreX + 150 + "px";
        }
        if (e.key == 'ArrowLeft') {
            dore = document.querySelector('.dore');
            doreX = parseInt(window.getComputedStyle(dore, null).getPropertyValue('left'));
            dore.style.left = (doreX - 150) + "px";
        }
    }

}


setInterval(() => {
    dore = document.querySelector('.dore');
    gameOver = document.querySelector('.gameOver');
    obstacle = document.querySelector('.obstacle');
    
        


    dx = parseInt(window.getComputedStyle(dore, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(dore, null).getPropertyValue('top'));

    ox = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('top'));

    offsetX = Math.abs(dx - ox);
    offsetY = Math.abs(dy - oy);
    console.log(offsetX, offsetY)
    if (offsetX < 45 && offsetY < 30) {
        gameOver.innerHTML = "Game Over - Reload to Play Again"
        obstacle.classList.remove('obstacleAni')
        audiogo.play();
        setTimeout(() => {
            audiogo.pause();
            audio.pause();
            gameIsOver = true;
            audiogo.play();
            setTimeout(()=>{
                

            },1);
        }, 1000);
    }
        

    else if (offsetX < 100 && cross && !gameIsOver) {
        score += 1;
        updateScore(score);
        cross = false;
        setTimeout(() => {
            cross = true;
        }, 1000);

        const randomScale = Math.random() * 0.5 + 1; 
        obstacle.style.transform = `scale(${randomScale})`; 

        setTimeout(() => {
            aniDur = parseFloat(window.getComputedStyle(obstacle, null).getPropertyValue('animation-duration'));
            newDur = aniDur - 0.1;
            obstacle.style.animationDuration = newDur + 's';
            console.log('New animation duration: ', newDur)
        }, 500);

    }

}, 10);

function updateScore(score) {
    if (!gameIsOver) {
        scoreCount.innerHTML = ("Your Score: " + score)
    }

}