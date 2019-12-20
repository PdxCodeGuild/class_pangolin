let conversions = {
  'ft': '.3084',
 'mi': '1609.34',
  'km':'1000',
 'm': '1',
  'yd':'.9144',
  'nchz':'.0254'
}

let message1 = "Enter the length / distance as a number: > "
let message2 = "Enter a starting uint as (ft, mi, km, m, yd, nchz): > "
let message3 = "Enter a conversion uint as (ft, mi, km, m, yd, nchz): > "

let user_starting_unit = prompt(message2)
let user_number_input = prompt(message1);
let user_unit_conversion_input = prompt(message3);

function convertToMeters(conversions, user_number_input){
Object.keys(conversions).forEach(function eachKey(key) { 
    if (key === user_starting_unit){
    return meters = (conversions[key] * user_number_input)
    }
  })
};

convertToMeters(conversions, user_number_input)
console.log(meters)

function convertToSelectedUnit(conversions, user_unit_conversion_input){
  Object.keys(conversions).forEach(function eachKey(key) { 
      if (key === user_unit_conversion_input){
      return conversion = ( meters / conversions[key])
      }
    })
  };

convertToSelectedUnit(conversions, user_unit_conversion_input)
console.log(conversion)
