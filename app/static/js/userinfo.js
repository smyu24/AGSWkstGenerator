function separate() {
	let value = document.getElementById("data").innerHTML;
	let myArr = value.split(',');
	myArr[1] = myArr[1]. slice(2, -1);
	myArr[6] = myArr[6]. slice(2, -2);
	let final = "Welcome " + myArr[1] + " " + myArr[6] + "!"
	document.getElementById("username").innerHTML =  final;
}

function display(text) {
	console.log(text);
}

function wkstopt() {
	var data = document.getElementById("lt").innerHTML;
	const myArr = data.split("',");
	
	var loctitle = 1;
	var locdesc = 2;
	for(let i = 0; i < parseInt(data.substring(2,6)); i++) {
		var col = document.createElement("div");
		col.className = "col";
		document.getElementById("rows").appendChild(col);

		var card = document.createElement("div");
		card.className = "card-panel hoverable small";
		card.id = "card" + i;
		card.setAttribute("onclick", 'display("' + myArr[loctitle].substring(2, (myArr[loctitle].length)) + '")');
		col.appendChild(card);

		var ctitle = document.createElement("div");
		ctitle.className = "card-panel-header";
		card.appendChild(ctitle);

		var hcard = document.createElement("span");
		hcard.className = "card-panel-icon";
		ctitle.appendChild(hcard);

		var title = document.createElement("i");
		title.className = "material-icons";
		title.textContent = myArr[loctitle].substring(2, (myArr[loctitle].length) );
		hcard.appendChild(title);

		var desc = document.createElement("p");
		desc.className = "card-panel-content";
		desc.textContent = myArr[locdesc].substring(2, (myArr[locdesc].length) );
		hcard.appendChild(desc);

		locdesc += 2;
		loctitle += 2;
	}
}

