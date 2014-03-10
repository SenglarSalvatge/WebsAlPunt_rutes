/*
 * JS DEL MAPA DE L'API DE GOOGLE MAPS V3: PART DE INSERCIO DE FORMULARIS
 */

//Declarem maps, que es de l'objecte mapa
//una marca d'inici 
//un array per guardar coordenades de linia
//un objecte linia

var map;
var marca;
var coordenadesLinia = [];
var liniaPath;
		
google.maps.event.addDomListener(window, 'load', inici);

function pinta_coords_si_hi_ha(){

	if($('#id_coordenades').val() != '') {
		//la cadena de coordenades s'ha de tractar
		//per tornar-la a tranformar en un objecte latlng
		var cadena = $('#id_coordenades').val();
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
		
		var splitter = splittejador[0].split(",");
		latlong = new google.maps.LatLng( $.trim( splitter[0] ),  $.trim( splitter[1]) );
		
		marca = new google.maps.Marker({
			position: latlong,
			map: map
		});
		marca.setMap(map);
		
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
//el primer cop que cargui el mapa, si es per editar el formulari serà ple


//aquesta funcion controla els events que li entren cada cop que cliquem
function inici() {
	
	//figueres: 42.254442,2.938843
	var centreMapa = new google.maps.LatLng(42.254442, 2.938843);
	var mapOptions = {
		zoom: 10,
		center: centreMapa,
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	//aqui controlem els click i guardem les coordenades
	google.maps.event.addListener(map, 'click', function(event) {
    	afegirMarca(event.latLng);
  	});

  	pinta_coords_si_hi_ha();
}
		
//afegim les coordenades a un array, per a generar una objecte Polyline
function afegirMarca(location) {
	//el primer clic hi posem una marca d'inici
  	if(marca == null) {
  		marca = new google.maps.Marker({
			position: location,
			map: map
		});
		marca.setMap(map);
  	} else {
  		marca.setMap(map);
  	}
		  	
  	//aquí muntem la linia
	coordenadesLinia.push(location);
	if (liniaPath == null) {
		liniaPath = new google.maps.Polyline({
		    path: coordenadesLinia,
		    geodesic: true,
		    strokeColor: '#FF0000',
		    strokeOpacity: 1.0,
		    strokeWeight: 2,
		    map: map
		  });
	} else {
		liniaPath.setPath(coordenadesLinia);
	}
  	liniaPath.setMap(map);
  	
  	serialitzarCoords(location);	
}
		
/*
 * Funció per serialitzar dades
 */
function serialitzarCoords(coordenades) {
	$('#id_coordenades').val($('#id_coordenades').val() + coordenades.toString());
}

/*
 * Funcions del control del panell
 */
function pintarLiniesAlMapa(map) {
  	liniaPath.setMap(map);
  	marca.setMap(map);
}

function amagarLinia() {
	pintarLiniesAlMapa(null);
}

function mostrarLinia() {
	pintarLiniesAlMapa(map);
}

function borrarLinia() {
	if(liniaPath != null) {
		$('#id_coordenades').val('');
		amagarLinia();
		coordenadesLinia = [];
		liniaPath = null;
		borrarMarca();
	}
}

function borrarMarca() {
	marca.setMap(null);
	marca = null;
}

function borrarUltimaMarca() {
	if(liniaPath != null) {
		if(coordenadesLinia.length == 1) {
		borrarMarca();
		liniaPath = null;
		coordenadesLinia = [];
		$('#id_coordenades').val('');
		} else {
			coordenadesLinia.pop();
			pintarLiniesAlMapa(null);
			pintarLiniesAlMapa(map);
			
			$('#id_coordenades').val('');
			
			for(var c in coordenadesLinia) {
				$('#id_coordenades').val($('#id_coordenades').val() + coordenadesLinia[c].toString());
			}
		}
	}
}


/* proves amb geolocalització que van ser fallides

$.ajax({
	type: "POST",
	url: "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyClNhahi1_H8Tmdb7_WeuGpd4YA1cfOPwk",
	data: x,
	})
	.done(function( msg ) {
		
});

var initialLocation;
var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var browserSupportFlag =  new Boolean();

if(navigator.geolocation) {
	browserSupportFlag = true;

	navigator.geolocation.getCurrentPosition(
		//success callback
		function(position) {
			initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
			map.setCenter(initialLocation);
		},
		//error callback
		function() {
			handleNoGeolocation(browserSupportFlag);
		});
} else {
	alert("Fallo");
	browserSupportFlag = false;
	handleNoGeolocation(browserSupportFlag);
}
*/

