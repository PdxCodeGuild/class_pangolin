let calc = 0

let msg1 = "Enter a number: > "
let msg2 = "Enter an operator (+, -, *, /): > "
let msg3 = "Enter a number: > "

let aNum = parseInt(prompt(msg1))
let usrOperator = prompt(msg2)
let bNum = parseInt(prompt(msg3))

let operators = {
  "+" : addFunct(aNum, bNum),
  "-" : subFunct(aNum, bNum),
  "*" : mulFunct(aNum, bNum),
  "/" : divFunct(aNum, bNum),
}

function  addFunct(aNum, bNum){
  return aNum + bNum
  
}
function  subFunct(aNum, bNum){
  return aNum - bNum
}
function  mulFunct(aNum, bNum){
  return aNum * bNum
}
function  divFunct(aNum, bNum){
  return aNum / bNum
}

function perfomrCalculation(operators, usrOperator){
  Object.keys(operators).forEach(function eachKey(key) { 
      if (key === usrOperator){
        console.log(operators[key])
        calc = operators[key]
        
      }
    })
    return calc
  };

 alert(perfomrCalculation(operators, usrOperator))
 