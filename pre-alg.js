/***********
 * Section 1 functions
 ***********/

//Check form condition
function checkform(min, max) {
	if(min < 99) { return false;}
	else if(max > 900) { return false;}
	else if(min > max) { return false;}
	else if(min == 0) { return false;}
	else if(max == 0) { return false;}
	return true;
}

//generating createdSeed
//[NUMprob][min][max] [NUMprob][min][max] [NUMprob][min][max] creation seed
function seedDefine() {
	const ids = ["numprob", "minnum", "maxnum"];
	const lvl = ["E","M", "H"];
	let combined = "";
	var createSeed = new Array();
	var j = 0;
	var total = 0;
	for(var i = 0; i < 3; i += 1) {
		combined = lvl[i].concat(ids[0]);
		var prob = parseInt(document.getElementById(combined).value);
		createSeed[j] = prob;
		total += prob;
		j += 1;

		combined = lvl[i].concat(ids[1]);
		var min = parseInt(document.getElementById(combined).value);
		createSeed[j] = min;
		j += 1;

		combined = lvl[i].concat(ids[2]);
		var max = parseInt(document.getElementById(combined).value);
		createSeed[j] = max;
		j += 1;

		if(prob > 0) {
			if(!checkform(min, max)) {
				return false;
			}
		}
	}

	if(total > 0) {
		return createSeed;
	} else {
		return false;
	}
}

//Generate the MASTERSEED
function send_section111(preseed) { //when request wkst form
	var masterSeed = "";
	var createSeed = seedDefine();

	if(createSeed == false) {
		alert("Please check the option before create the worksheet.");
	} else {
		preseed = document.getElementById("seed").innerHTML;
		for(var j = 0; j < 9; j += 3) {
			for(var i = 0; i < createSeed[j]; i += 1) {
				masterSeed = masterSeed.concat( section1(createSeed[j+1], createSeed[j+2]) );
			}
		}

		//remove previous p
		document.getElementById("wks-problems").textContent = "";
		showPDF(masterSeed);

		//FINAL stage
		masterSeed = preseed + "&&" + masterSeed;
		document.getElementById("master").value = createSeed;
	}
}

//Change the display setting to the block
function showPDF(seed) {
	var element = document.getElementsByClassName("col-worksheet");

	for (var i = 0; i < element.length; i++) {
		element[i].style.display = "block";
	}

	var element2 = document.getElementsByClassName("upload");

	for (var i = 0; i < element2.length; i++) {
		element2[i].style.display = "block";
	}

	var name = document.getElementById("studnetName").value;
	document.getElementById("txt-studnetName").innerHTML = name;
	var date = document.getElementById("dueDate").value;
	document.getElementById("txt-dueDate").innerHTML = date;

	//Desc
	document.getElementById("txt-title").innerHTML = document.getElementById("pdftitle").value;
	document.getElementById("txt-desc").innerHTML = document.getElementById("pdfdesc").value;

	var divs = document.createElement('div');
	divs.innerHTML = seed;
	const typeset = document.querySelector('#wks-problems')
	typeset.appendChild(divs)
	setTimeout(function () {
		MathJax.typeset()
		typeset.appendChild(divs)
	  }, 10)
}

//Generate random problems
function sec1rand(min, max) {return Math.floor((Math.random() * (max - min + 1)) + min);}
function section1(min, max) { //difficulty, minimum, maximum
	var digit = sec1rand(1, 3), //define the value
	num = sec1rand(min, max),
	s_num = num.toString(),
	prob = "\\overline{b}",
	arr = [],
	problem = "";

	//into char
	s_num = num.toString();
	for(var i = 0; i < s_num.length; i += 1) {
		arr.push(+s_num.charAt(i));
	}

	//replace & combine
	if(digit == 1) {
		problem = "\\(" + prob.replace("b", arr[0]) + arr[1] + arr[2] + "\\)"; }
	else if(digit == 2) {
		problem = "\\(" + arr[0] + prob.replace("b", arr[1]) + arr[2] + "\\)"; }
	else {
		problem = "\\(" + arr[0] + arr[1] + prob.replace("b", arr[2]) + "\\)"; }

	return problem
}
