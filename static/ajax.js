function postParas() {
	var start = ""
	var amount = document.getElementById("amount").value;
	var length = document.getElementById("length").value;
	var query = window.location.search;

	var formData = new FormData();
	formData.append("start", start);
	formData.append("amount", amount);
	formData.append("length", length);

	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("post", "/test" + query, true);
	xmlHttp.send(formData);
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
			alert(xmlHttp.responseText);
			window.location = "http://" + window.location.host + "/result"
		}
	};
}