function testDifficulty(list) { //creating dynamic difficulty
	document.getElementById("level").innerHTML = "";

	len = diff[list][0].split(",");
    var label = document.createElement("label");
    label.className = "num-problem-font";
    label.textContent = "Section Field*";
    document.getElementById("level").appendChild(label);

    var select = document.createElement("select");
    select.id = "levels";
    select.name = "level" + list;
    select.required = "True";
    for(let i = 0; i < len.length; i++) {
        select.innerHTML += '<option value="' + (i+1) + '">' + len[i] + '</option>';
    }

    document.getElementById("level").appendChild(select);
    if(len.length == 0) {
        document.getElementById("level").style.display = "none";
    }
}

function testSelection(list) { //creating dynamic selection
	document.getElementById("select").innerHTML = "";

	len = section[list][0].split(",");
    var label = document.createElement("label");
    label.className = "num-problem-font";
    label.textContent = "Learning Target*";
    document.getElementById("select").appendChild(label);

    var select = document.createElement("select");
    select.id = 'Ltarget' + list;
    select.name = 'Ltarget' + list;
    select.value = 0;
    for(let i = 0; i < len.length; i++) {
        select.innerHTML += '<option value="' + (i+1) + '">' + len[i] + '</option>';
    }
    select.required = "True";
    document.getElementById("select").appendChild(select);
}

function list_prealgebra() { //displaying note for the test module
	for(let i = 0; i < ex.length; i++) {
		var lnk = document.createElement('li');
		var adiv = document.createElement('a');

		lnk.appendChild(adiv);
		lnk.id = "lst_font";
		lnk.className = 'b';

		adiv.innerText = (desc[i][0].split('|'))[0];
		adiv.id = i;
		adiv.className = ex[i] + " asize";
		adiv.setAttribute("onclick", 'open_option("' + ex[i] + '", "' + i + '")');

		var breakdiv = document.createElement('div');
		breakdiv.id = "a"+i;
		lnk.appendChild(breakdiv);

		var note = document.createElement('div');
		note.className = "globalnote";
		note.id = "note" + i;

		note.innerText = noted[i];
		note.style = "display: none;"

		document.getElementById("childs").appendChild(lnk);
		document.getElementById("a"+i).appendChild(note);

	}
}

function open_option(seed, val) {
	clicked = val;
	sd = seed;
	inserttable();
}

function deltable() {
	document.getElementById("option-bar").style.display = "none";
}

function inserttable() { //table elements
	var table = document.getElementById("sortable");
	var row = table.insertRow(table.rows.length);
	var title = row.insertCell(0);
	var sections = row.insertCell(1);
	var difficulty = row.insertCell(2);
	var numofprob = row.insertCell(3);

	title.innerHTML = document.getElementById(clicked).innerText;
	row.id = sd;
	row.className = table.rows.length - 1;

	var sec = document.createElement("select"); //section
	lens = section[clicked][0].split(",");

	for(let i = 0; i < lens.length; i++) {
		sec.innerHTML += '<option value="' + (i+1) + '">' + lens[i] + '</option>';
	}
	sec.required = "True";
	sections.appendChild(sec);

	var sel = document.createElement("select");
	len = diff[clicked][0].split(",");
	for(let i = 0; i < len.length; i++) {
		sel.innerHTML += '<option value="' + (i+1) + '">' + len[i] + '</option>';
	}
	sel.required = "True";
	difficulty.appendChild(sel);

	var numput = document.createElement("input");
	numput.type = "number";
	numput.value = 25;
	numput.min = 1;
	numput.max = 2000;
	numofprob.appendChild(numput);

	var btndel = document.createElement("button");
	btndel.style = "margin-left: 18px; background: none; border: none;";
	btndel.className = "btnDelete";

	var deli = document.createElement("i");
	deli.className = "fa fa-minus-circle";
	btndel.appendChild(deli);
	numofprob.appendChild(btndel);

	for(let i = 0; i < table.rows.length; i++) {
		table.rows[i].cells[1].childNodes[0].id = "sec" + i;
		table.rows[i].cells[2].childNodes[0].id = "dif" + i;
		table.rows[i].cells[3].childNodes[0].id = "tnum" + i;
    }

	relabelseed();
}

//Define the pre-set of the test
function testwkstopt() {
	var loctitle = 1;
	var locdesc = 2;
	for(let i = 0; i < set.length; i++) {

		var col = document.createElement("div");
		col.className = "col";
		document.getElementById("rows").appendChild(col);

		var card = document.createElement("div");
		card.className = "card-panels hoverable small";
		card.id = "card" + i;
		col.appendChild(card);

		var ctitle = document.createElement("div");
		ctitle.className = "card-panels-header";
		card.appendChild(ctitle);

		var hcard = document.createElement("span");
		hcard.className = "card-panels-icon";
		ctitle.appendChild(hcard);

		var btncreate = document.createElement("div");
		btncreate.className = "settitle";

		var sectitle = document.createElement("p");
		sectitle.className = "testtitle";
		sectitle.innerText = set[i][0];

		var btntest = document.createElement("button");
		btntest.className = "btntest";
		btntest.innerText = "Take a test";
		//btntest.type = "submit";
		btntest.setAttribute("onclick", 'sendtoserver("' + set[i][2] + '")');


		btncreate.appendChild(sectitle);
		btncreate.appendChild(btntest);
		card.appendChild(btncreate);

		var title = document.createElement("i");
		title.className = "material-icons";
		title.textContent = set[i][1];
		hcard.appendChild(title);

		var desc = document.createElement("p");
		desc.className = "card-panels-content";
		desc.textContent = set[i][3];
		hcard.appendChild(desc);

		locdesc += 2;
		loctitle += 2;
	}
}

function gotoadv() {
	location.replace("/test/adv");
}

function sendtoserver(id) {
	arr = id.replaceAll('.', '-').split(",");
	lst = []
	for(let i = 0; i < arr.length; i++) {
		if(arr[i].substring(0, 4) == "pre-") { //if prealgebra
			lst[i] = arr[i].substring(4, arr[i].length);
		}
	}
	document.getElementById("seed").value = lst;
}

function insertcustomtable(seed, location, numsec, diffi, num) { //table elements
	var table = document.getElementById("sortable");
	var row = table.insertRow(table.rows.length);
	var title = row.insertCell(0);
	var sections = row.insertCell(1);
	var difficulty = row.insertCell(2);
	var numofprob = row.insertCell(3);

	title.innerHTML = document.getElementById(location).text;
	row.id = seed;
	row.className = table.rows.length - 1;

	var sec = document.createElement("select");
	lens = section[location][0].split(",");

	for(let i = 0; i < lens.length; i++) {
		if(numsec == (i+1) ) {
			sec.innerHTML += '<option selected="selected" value="' + (i+1) + '">' + lens[i] + '</option>';
		} else {
			sec.innerHTML += '<option value="' + (i+1) + '">' + lens[i] + '</option>';
		}
	}
	sec.required = "True";
	sections.appendChild(sec);

	var sel = document.createElement("select");
	len = diff[location][0].split(",");
	for(let i = 0; i < len.length; i++) {
		sel.innerHTML += '<option value="' + (i+1) + '">' + len[i] + '</option>';
	}
	sel.required = "True";
	difficulty.appendChild(sel);

	var numput = document.createElement("input");
	numput.type = "number";
	numput.value = 25;
	numput.min = 1;
	numput.max = 2000;
	numofprob.appendChild(numput);

	var btndel = document.createElement("button");
	btndel.style = "margin-left: 18px; background: none; border: none;";
	btndel.className = "btnDelete";

	var deli = document.createElement("i");
	deli.className = "fa fa-minus-circle";
	btndel.appendChild(deli);
	numofprob.appendChild(btndel);

	for(let i = 0; i < table.rows.length; i++) {
		table.rows[i].cells[1].childNodes[0].id = "sec" + i;
		table.rows[i].cells[2].childNodes[0].id = "dif" + i;
		table.rows[i].cells[3].childNodes[0].id = "tnum" + i;
    }

	relabelseed();
}

function enterpretable() {
	for(let j = 0; j < psed.length; j++) {
		var loc = 0;
		for(let i = 0; i < ex.length; i++) {
			if(ex[i].toString().replace(/\s/g, '') == psed[j].toString().replace(/\s/g, '')) {
				loc = i;
			}
		}

		for(let i = 1; i <= psec[j]; i++) {
			insertcustomtable(psed[j], loc, i, 1, 25); //seed, section, difficulty, number of problem
		}
	} //end of the main for loop
}

function relabelseed() {
	var table = document.getElementById("sortable");

    document.getElementById("seed").value = ""
    for(let i = 0; i < table.rows.length; i++) {
		tsec = document.getElementById("sec" + table.rows[i].className).options[document.getElementById("sec" + table.rows[i].className).value-1].value;
		tdif = document.getElementById("dif" + table.rows[i].className).options[document.getElementById("dif" + table.rows[i].className).value-1].value;
		tnum = document.getElementById("tnum" + table.rows[i].className).value;

      	document.getElementById("seed").value += table.rows[i].id + ",-" + tsec + "," + tdif + "," + tnum;

	  if(i != table.rows.length-1) {
		document.getElementById("seed").value += ", ";
	  }
    }
}

//change instruction for the test
function testdisplayinst(data) {
    for(let i = 0; i < total; i++) {
        document.getElementById("subpdfdesc" + (i+1)).innerText = data[i];
    }
    changecol(wkst);
}