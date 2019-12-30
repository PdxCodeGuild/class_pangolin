let conversions = {
  'ft': '.3084',
  'mi': '1609.34',
  'km':'1000',
  'm': '1',
  'yd':'.9144',
  'nchz':'.0254'
}

let user_starting_unit = document.querySelector('#strt_unit')
let user_number_input = document.querySelector('#number')
let user_unit_conversion_input = document.querySelector('#conv_unit')
let meters = 0;
let conversion = 0;
  
submit_btn.onclick = function() {
    function convertToMeters(conversions, user_number_input){
      Object.keys(conversions).forEach(function eachKey(key) {
        if (key === user_starting_unit.value){
          return meters = (conversions[key] * parseInt(user_number_input.value))
        }
      })
    };

  convertToMeters(conversions, user_number_input)
  
    function convertToSelectedUnit(conversions, user_unit_conversion_input, meters){
      Object.keys(conversions).forEach(function eachKey(key) {
        if (key === user_unit_conversion_input.value){
          conversion = ( meters / conversions[key])
        }
      })
    };

  convertToSelectedUnit(conversions, user_unit_conversion_input, meters)

  output_div.innerText = conversion;
}