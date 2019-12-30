var urls = new Array();
urls[0] = 'https://explore.org/livecams/kitten-rescue/kitten-rescue-baby-kittens';
urls[1] = 'https://bestlifeonline.com/puppies-other-animals/';
urls[2] = 'https://www.boredpanda.com/cute-baby-elephants/?utm_source=googleutm_medium=organic&utm_campaign=organic';

var random = Math.floor(Math.random() * urls.length);

window.location = urls[random];