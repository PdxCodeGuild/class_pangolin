// Airmap API key here
let airmapkey = '$!'

let map, drawingManager;
    
// Azure map template    
function GetMap() {
    //Initialize a map instance.
    map = new atlas.Map('myMap', {
        center: [-122.67305676538223, 45.50631212151009], // Center map on this location
        zoom: 12,
        view: 'Auto',
        style: "grayscale_dark", // Map color "dark themed"

//Add your Azure Maps subscription key to the map SDK. Get an Azure Maps key at https://azure.com/maps
        authOptions: {
            authType: 'subscriptionKey',
            subscriptionKey: '$!' // Place Azure subscription key here
        }
    });

    //Wait until the map resources are ready.
    map.events.add('ready', function () {

      let layers = map.map.getStyle().layers;

        //Create an instance of the drawing manager and display the drawing toolbar.
        drawingManager = new atlas.drawing.DrawingManager(map, {
            toolbar: new atlas.control.DrawingToolbar({ position: 'top-right', style: 'dark' })
        });
    });
    
}

// Variable which holds map position data
let mapLocationData = ""

// Function which gathers map position for API request 
function getDrawnShapes() {
    let source = drawingManager.getSource();
    
    mapLocationData = source.toJson();
    return mapLocationData
}

// Button for submitting API request to Airmap
Vue.component('btn_s1', {
 
  template: `

  <button 
  class="btn btn-secondary btn-sm"
  style="background-color: rgba(102, 102, 102, 0.39); box-shadow: 0px 0px 15px #888888b0;"
  @click="$emit('r1submit')">Submit</button>
  
  `
});

let vm = new Vue({
  el: '#app',
  data: {
    airSpaceData: {}
  },
  methods: {
    getTestData: function() {
      console.log(mapLocationData.features[0].geometry.coordinates, "test test");
    },
    getData(){
      axios.post('https://api.airmap.com/rules/v1', {
      }, {
        headers: {
          'X-API-Key': airmapkey,
            'Content-Type': 'application/json; charset=UTF-8'
        },
        data: {
          "geometry": {
            "type": "Point",
            "coordinates": mapLocationData.features[0].geometry.coordinates,
          }

        }
      })
      .then(response => { 
        (this.airSpaceData = response.data.data)
        console.log(response)
      })
      
      .catch(error => {
          console.log(error.response)
      })
     }
  },
  mounted: function() {
    // console.log("It loaded!");
  }
});

