let conversions = {
  ft: '.3084',
  mi: '1609.34',
  km:'1000',
  m: '1',
  yd:'.9144',
  nchz:'.0254'
}

console.log(Object.values(conversions))
console.log(Object.keys(conversions))


let message1 = "Enter the length / distance as a number: > "
let message2 = "Enter a starting uint as (ft, mi, km, m, yd, nchz): > "
let message3 = "Enter a conversion uint as (ft, mi, km, m, yd, nchz): > "

let user_starting_unit = prompt(message2)


for (let key of Object.keys(conversions)) {
  if (key == user_starting_unit)
  console.log("here")
}

// let user_number_input = prompt(message1);
// let user_unit_conversion_input = prompt(message3);

// alert("Return results here");

// converts usre inputs to meters
// function conver_to_meters(param) {  

// }

// converts from meters to desired unit
// function conver_to_meters(param) {  }

// for key, value in conversions.items():
//      if key == user_starting_unit:
//          to_meters = value * user_number_input

// for key, value in conversions.items():
// if key == user_unit_conversion_input:
//           print(to_meters / value)