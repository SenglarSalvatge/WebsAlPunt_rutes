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

//aquesta funcion controla els events que li entren cada cop que cliquem
function inici() {
	document.getElementById('postCoordenades').value = '';
	var centreMapa = new google.maps.LatLng(42.5673, 3);
	var mapOptions = {
		zoom: 15,
		center: centreMapa,
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	//aqui controlem els click i guardem les coordenades
	google.maps.event.addListener(map, 'click', function(event) {
    	afegirMarca(event.latLng);
  	});
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
	document.getElementById('postCoordenades').value += coordenades.toString();
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
		document.getElementById('postCoordenades').value = '';
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
		document.getElementById('postCoordenades').value = '';
		} else {
			coordenadesLinia.pop();
			pintarLiniesAlMapa(null);
			pintarLiniesAlMapa(map);
			
			document.getElementById('postCoordenades').value = '';
			
			for(var c in coordenadesLinia) {
				document.getElementById('postCoordenades').value += coordenadesLinia[c].toString();
			}
		}
	}
	
}