// JavaScript File

var borderslayer = L.geoJson(null, { style: get_style, onEachFeature:onEachFeature });

    function resetHighlight(e) {
		borderslayer.resetStyle(e.target);
		info.update();
	}

	function onEachFeature(feature, layer) {
		layer.on({
			mouseover: highlightFeature,
			mouseout: resetHighlight
			
		});
	}

	omnivore.geojson('mos_districts.geojson', null, borderslayer);

	borderslayer.addTo(map);