//THIS IS THE NOTE PAGE FOR JS


//API
- this stand for "applicatio programming interface"
- a standardized way to send and receive data from a web service via HTTP request
-

important!
we are sending literals when sending info. This look just like what you type in the text editor

//AJAX
- "asynchronous javascript and XML"
- allows you to execute HTTP requests from JavaScript, without reloading the page.

-- create a new XMLHttpRequest()
-- put event listners on the request ( progress, error, load, abort) <= these are the 4 possible events 
-- open the request. this is where you will be putting a Method(get, post, put, delete) 
-- alot of the time you will make a url that is dynamicly generated and modified by user Input
-- optional step is to set an request headers these put in a token to make it more secure 
-- send the request easy as req.send()
---------------------------
Handle the response:
-- parse the response back into JavaScript JSON.parse()
-- put it into html and display to the page. 
-- if you are having this load on click you need to set it to click addEventListener()

There are two ways to do all this using Fetch and  es6 Promises , Axios



Axios: github/ axios / axios
is a JavaScript library that you actually have to load with a script tag
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>


EXAMPLE:
Super Basic:

axios.get(url)
.then(function (response) {
  console.log(response.data)
})

A Little More: (this one just has a url and  config headers)

let config = {
    headers: {
      'x-api-key': api_key
    }
  }
  axios.get(url, config)
  .then(function (response) {
    console.log(response.data)
  })
  
  There are even more check out the github page for Axios Api and you will see!

  url:always put in
  method: always put in

  baseURL: this can be a constant url and the upper url can be the one that is changing and get other stuff with 
  transformRequest:
  return data
----------------------------------
This is a example of how to write a axios api request : and all this goes inside a addEventListener();

axios({
    url: "the site your going to",
    method: "GET",
    headers: {
        Authorization: 'Token token=kldjkfkakkfda;ldf stuf'
    }
}).then(function(response){
    let resultHTML = `
    <p>${response.data.quote.body}</p>
    <p><i><a href="${response.data.quote.url}">${response.data.quote.author}</a></i></p>
    `
    target.innerHTML = resultHTML;
}).catch(function(error){
    console.log(error);
})