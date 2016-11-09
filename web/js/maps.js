// JavaScript File

	var map;	
	
    function highlightFeature(e) {
		var layer = e.target;

		layer.setStyle({
			weight: 5,
			color: '#666',
			dashArray: '',
			fillOpacity: 0.7
		});

		if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
			layer.bringToFront();
		}

		info.update(layer.feature.properties);
	}
    
	
	var resize = function () {
		var $map = $('#map');
		$map.height($(window).height() - $('div.navbar').outerHeight());
		if (map) {
			map.invalidateSize();
		}
	};
	
	$(window).on('resize', function () {
		resize();
	});
	resize();

	map = L.map('map').setView([55.7256992,37.5878394], 10);
	map.setMaxBounds(L.latLngBounds(L.latLng(56.0676,38.4466),L.latLng(55.1098,36.6448)));
	map.setMinZoom(10);
	
	var defStyle = { color: "#420000", fillColor: '#FED976', fillOpacity: 0.1, weight: 1 };

	var defColor = "#f8e478";
	
	var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">' +
        'OpenStreetMap</a> contributors';
    var osm = L.tileLayer(osmUrl, {
        maxZoom: 18,
        attribution: osmAttrib,
        noWrap: true
      }).addTo(map);
      
    
	var legend = L.control({position: 'bottomright'});
	
		// control that shows state info on hover
	var info = L.control();

	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};

    
      