let calc = 0

let aNum = document.querySelector('#aNumInp')
let usrOperator = document.querySelector('#usrOperatorInp')
let bNum = document.querySelector('#bNumInp')


function  addFunct(aNum, bNum){
  calc = aNum + bNum
 
}
function  subFunct(aNum, bNum){
  calc = aNum - bNum
  return calc
}
function  mulFunct(aNum, bNum){
  calc = aNum * bNum
  return calc
}
function  divFunct(aNum, bNum){
  calc = aNum / bNum
  return calc
}

function perfomrCalculation(aNum, bNum, usrOperator){
let nacho = usrOperator.value 
let num1 = parseInt(aNum.value)
let num2 = parseInt(bNum.value)
    
  if (nacho === "+") {
      addFunct(num1, num2);
  } else if (nacho === "-") {
      subFunct(num1, num2);
  } else if (nacho === "*") {
      mulFunct(num1, num2);
  } else if (nacho === "/"){
      divFunct(num1, num2);
  }

};


submit_btn.onclick = function() {
  perfomrCalculation(aNum, bNum, usrOperator)
  output_div.innerText = calc;
    };
   

    
