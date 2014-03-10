var map;
var marca1;
var marca2;
var coordenadesLinia = [];
var liniaPath;
		

function pinta(){
	
	//centre figueres : 42.254442, 2.938843
	var centreMapa = new google.maps.LatLng(42.254442, 2.938843);
	var mapOptions = {
		zoom: 10,
		center: centreMapa,
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	
	
	if($('#coordenades').val() != '') {
		//la cadena de coordenades s'ha de tractar
		//per tornar-la a tranformar en un objecte latlng
		var cadena = $('#coordenades').val();
		cadena = cadena.substr(1,cadena.length);
		cadena = cadena.substr(0, cadena.length - 1);
		var splittejador = cadena.split(")(");
		
		coordenadesLinia = [];
		var latlong;
		for(var tupla in splittejador) {
			var splitter = splittejador[tupla].split(",");
			latlong = new google.maps.LatLng( $.trim( splitter[0] ),  $.trim( splitter[1]) );
			coordenadesLinia.push(latlong);
		}
		
		//marca final
		marca2 = new google.maps.Marker({
			position: latlong,
			map: map
		});
		marca2.setMap(map);
		
		//==========
		
		var splitter = splittejador[0].split(",");
		latlong = new google.maps.LatLng( $.trim( splitter[0] ),  $.trim( splitter[1]) );
		
		//marca inicial
		marca1 = new google.maps.Marker({
			position: latlong,
			map: map
		});
		marca1.setMap(map);
		
		//========
		
		liniaPath = new google.maps.Polyline({
			    path: coordenadesLinia,
			    geodesic: true,
			    strokeColor: '#FF0000',
			    strokeOpacity: 1.0,
			    strokeWeight: 2,
			    map: map
		});
		liniaPath.setMap(map);
		
		map.setCenter(latlong);
		map.setZoom(13);
		
	}
}

$(document).ready(function(){
	pinta();
	google.maps.event.addListener(marca1, 'click', toggleBounce);
	google.maps.event.addListener(marca2, 'click', toggleBounce);
});




function toggleBounce() {

  if (marca1.getAnimation() != null) {
    marca1.setAnimation(null);
    marca2.setAnimation(null);
  } else {
    marca1.setAnimation(google.maps.Animation.BOUNCE);
    marca2.setAnimation(google.maps.Animation.BOUNCE);
  }
}

