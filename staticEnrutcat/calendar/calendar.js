$(function() {
	$.datepicker.regional['cat'] = {
	  closeText: 'Tancar',
	  prevText: 'Previ',
	  nextText: 'Següent',
	   
	  monthNames: ['Gener','Febrer','Març','Abril','Maig','Juny',
	  'Juliol','Agost','Septembre','Octubre','Novembre','Desembre'],
	  monthNamesShort: ['Gen','Feb','Mar','Abr','Mai','Jun',
	  'Jul','Ago','Sep','Oct','Nov','Des'],
	  monthStatus: 'Veure un altre mes', yearStatus: 'Veure un altre any',
	  dayNames: ['Diumenge','Dilluns','Dimarts','Dimecres','Dijous','Divendres','Dissabte'],
	  dayNamesShort: ['Dium','Dill','Dim','Dime','Dij','Div','Dis'],
	  dayNamesMin: ['Dium','Dill','Dim','Dime','Dij','Div','Dis'],
	  dateFormat: 'dd/mm/yy', firstDay: 1,
	  initStatus: 'Selecciona La data', isRTL: false};
	  
	  $.datepicker.setDefaults($.datepicker.regional['cat']);
	  
	  //miDate: fecha de comienzo D=días | M=mes | Y=año
	  //maxDate: fecha tope D=días | M=mes | Y=año
	  $( ".datepicker" ).datepicker({ minDate: "-1D", maxDate: "+1M +10D" });
});