function checkstatus() {
	
	$.get('log.txt', function(data) {
		var array = data.split("\n");
		
		var index;
		var writelist = "";
		var btnVar = "";
		for (index = 0; index < array.length - 1; index++) {
			var arrayitem = array[index].split(";");
			if (arrayitem[0] === "ONLINE") {
				btnVar = "btn-success"
			} else {
				btnVar = "btn-danger"
			}
		    writelist += "<p class='list-group-item'>"+ arrayitem[1] + "<button type='button' class='btn btn-sm float-right "+btnVar+"'>"+ arrayitem[0] +"</button></p>";
		}
		document.getElementById("datalist").innerHTML = writelist;

	}, 'text');

}