let jackalopes = [0, 0];
let counter = 0;
console.log(jackalopes);
while (jackalopes.length < 1000) {
    for (let i=0; i<jackalopes.length; i++) {
        jackalopes[i] ++
    }
    console.log(jackalopes);
    
    for (let i=0; i<=jackalopes.length; i++) {
        if (jackalope in range(4,9)) {
            jackalopes.push(0)
        }
    }
    for (let i=0; i<(jackalopes.length - 1); i++) {
        if (jackalopes[i] === 10) {}       
            jackalopes.splice(i, 1)
    }
    console.log(jackalopes) 
    counter ++   
}   
   console.log(counter)
   console.log(jackalopes.length)      