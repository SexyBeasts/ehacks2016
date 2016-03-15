$(document).ready(function(){
	update();
	function update() {
		$.ajax ({
			success : function() {
				document.getElementById("audioPlayer").setAttribute("src", document.getElementById("input"));
			}
		})
	}
});
  