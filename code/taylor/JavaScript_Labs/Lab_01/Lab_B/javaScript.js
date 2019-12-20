var userArray = []; // User input array
var maxLength = 10; // Max array length
var total = 0; // Variable initialization for summing user array values

for(var i=0; i<maxLength; i++) {  // For loop, receives input up to maxLength value
	
	userArray[i] = parseInt(prompt('Enter a Number: ' + (i+1)));
}

for(var i = 0; i < userArray.length; i++) {
    total += userArray[i];
}
console.log(total / userArray.length);


