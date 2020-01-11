// // Vue component template
// Vue.component('component-name', {
//     props: [],
//     data: function () {
//         return {

//         }
//     },
//     template: ``,
//     methods: {},
//     computed: {},
//     mounted(){},
// })

// Vue app template
let vm = new Vue({
    el: "#app",
    data: {
        map: null,
        drawingManager: [],
        placeIdArray: [],
        polylines: [],
        snappedCoordinates: [],
    },
    methods: {
        initialize: function () {
            console.log("intializing")
            var mapOptions = {
                zoom: 17,
                center: { lat: -33.8667, lng: 151.1955 }
            };
            this.map = new google.maps.Map(document.getElementById('map'), mapOptions);

            // Adds a Places search box. Searching for a place will center the map on that
            // location.
            this.map.controls[google.maps.ControlPosition.RIGHT_TOP].push(
                document.getElementById('bar'));
            var autocomplete = new google.maps.places.Autocomplete(
                document.getElementById('autoc'));
            autocomplete.bindTo('bounds', this.map);
            autocomplete.addListener('place_changed', function () {
                var place = autocomplete.getPlace();
                if (place.geometry.viewport) {
                    this.map.fitBounds(place.geometry.viewport);
                } else {
                    this.map.setCenter(place.geometry.location);
                    this.map.setZoom(17);
                }
            });

            // Enables the polyline drawing control. Click on the map to start drawing a
            // polyline. Each click will add a new vertice. Double-click to stop drawing.
            this.drawingManager = new google.maps.drawing.DrawingManager({
                drawingMode: google.maps.drawing.OverlayType.POLYLINE,
                drawingControl: true,
                drawingControlOptions: {
                    position: google.maps.ControlPosition.TOP_CENTER,
                    drawingModes: [
                        google.maps.drawing.OverlayType.POLYLINE
                    ]
                },
                polylineOptions: {
                    strokeColor: '#696969',
                    strokeWeight: 2
                }
            });
            this.drawingManager.setMap(this.map);

            // Snap-to-road when the polyline is completed.
            this.drawingManager.addListener('polylinecomplete', function (poly) {
                var path = poly.getPath();
                this.polylines.push(poly);
                this.placeIdArray = [];
                this.runSnapToRoad(path);
            });


        },
        // Snap a user-created polyline to roads and draw the snapped path
        runSnapToRoad: function (path) {
            var pathValues = [];
            for (var i = 0; i < path.getLength(); i++) {
                pathValues.push(path.getAt(i).toUrlValue());
            }

            $.get('https://roads.googleapis.com/v1/snapToRoads', {
                interpolate: true,
                key: apiKey,
                path: pathValues.join('|')
            }, function (data) {
                processSnapToRoadResponse(data);
                drawSnappedPolyline();
                getAndDrawSpeedLimits();
            });
        },
        // Store snapped polyline returned by the snap-to-road service.
        processSnapToRoadResponse: function (data) {
            this.snappedCoordinates = [];
            this.placeIdArray = [];
            for (var i = 0; i < data.snappedPoints.length; i++) {
                var latlng = new google.maps.LatLng(
                    data.snappedPoints[i].location.latitude,
                    data.snappedPoints[i].location.longitude);
                snappedCoordinates.push(latlng);
                this.placeIdArray.push(data.snappedPoints[i].placeId);
            }
        },
        // Draws the snapped polyline (after processing snap-to-road response).
        drawSnappedPolyline: function () {
            var snappedPolyline = new google.maps.Polyline({
                path: snappedCoordinates,
                strokeColor: 'black',
                strokeWeight: 3
            });

            snappedPolyline.setMap(map);
            this.polylines.push(snappedPolyline);
        },
        // Gets speed limits (for 100 segments at a time) and draws a polyline
        // color-coded by speed limit. Must be called after processing snap-to-road
        // response.
        getAndDrawSpeedLimits: function () {
            for (var i = 0; i <= placeIdArray.length / 100; i++) {
                // Ensure that no query exceeds the max 100 placeID limit.
                var start = i * 100;
                var end = Math.min((i + 1) * 100 - 1, this.placeIdArray.length);

                this.drawSpeedLimits(start, end);
            }
        },
        // Gets speed limits for a 100-segment path and draws a polyline color-coded by
        // speed limit. Must be called after processing snap-to-road response.
        drawSpeedLimits: function (start, end) {
            var placeIdQuery = '';
            for (var i = start; i < end; i++) {
                placeIdQuery += '&placeId=' + this.placeIdArray[i];
            }

            $.get('https://roads.googleapis.com/v1/speedLimits',
                'key=' + apiKey + placeIdQuery,
                function (speedData) {
                    this.processSpeedLimitResponse(speedData, start);
                }
            );
        },
        // Draw a polyline segment (up to 100 road segments) color-coded by speed limit.
        processSpeedLimitResponse: function (speedData, start) {
            var end = start + speedData.speedLimits.length;
            for (var i = 0; i < speedData.speedLimits.length - 1; i++) {
                var speedLimit = speedData.speedLimits[i].speedLimit;
                var color = this.getColorForSpeed(speedLimit);

                // Take two points for a single-segment polyline.
                var coords = snappedCoordinates.slice(start + i, start + i + 2);

                var snappedPolyline = new google.maps.Polyline({
                    path: coords,
                    strokeColor: color,
                    strokeWeight: 6
                });
                this.snappedPolyline.setMap(map);
                this.polylines.push(snappedPolyline);
            }
        },
        getColorForSpeed: function (speed_kph) {
            if (speed_kph <= 40) {
                return 'purple';
            }
            if (speed_kph <= 50) {
                return 'blue';
            }
            if (speed_kph <= 60) {
                return 'green';
            }
            if (speed_kph <= 80) {
                return 'yellow';
            }
            if (speed_kph <= 100) {
                return 'orange';
            }
            return 'red';
        },
        // Clear button. Click to remove all polylines.
        clear: function(ev) {
            for (var i = 0; i < this.polylines.length; ++i) {
                this.polylines[i].setMap(null);
            }
            this.polylines = [];
            ev.preventDefault();
            return false;
        },
    },
    computed: {

    },
    mounted() {
        this.initialize();
    }
});


