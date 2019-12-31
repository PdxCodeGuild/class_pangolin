function startTimer(duration, display) {
  let timer = duration, seconds;
  let url_lst = [ 'https://www.drudgereport.com',
                  'https://www.yahoo.com',
                  'https://www.bing.com',
                  'https://www.gizmodo.com',
                  'https://www.cnn.com',
                ]
  let destination = Math.floor(Math.random()*url_lst.length);
  
  setInterval(function () {
      seconds = parseInt(timer % 60, 10);
      seconds = seconds < 10 ? "0" + seconds : seconds;
      display.textContent = seconds;

      if (-- timer <= -2) {
        
        window.location = url_lst[destination];
        alert(`You're headed to ${url_lst[destination]}`)
      }

    }, 1000);
}

window.onload = function () {
  var tenSeconds = 1 * 10,
      display = document.querySelector('#time');
  startTimer(tenSeconds, display);
};