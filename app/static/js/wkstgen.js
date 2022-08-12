function keepchange(ele) {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var chkdate = document.getElementById("ckdueDate").checked;
	var date = document.getElementById("dueDate").value;

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(date != "") {
	date = "\\head{AGS Worksheet Generator}{Due Date: " + date + "}";
	newfront = newfront.replace("\\head{AGS Worksheet Generator}{Due Date: MM/DD/YYYY}", date);
	}
	if(chkdate == false) {
		newfront = newfront.replace(date, "\\head{AGS Worksheet Generator}{}");
	}

	return newfront + changecolrow(newcol, newrow, ele) + backtex;
}
function uppdf() {
	var runlatexLatexcgiURI="https://texlive.net/cgi-bin/latexcgi";
    var f2 = document.createElement("span");
		    f2.innerHTML="<form style=\"display:none\" id=\"form2-pre" + 0 +
			"\" name=\"form2-pre" + 0 +
			"\" enctype=\"multipart/form-data\" action=\"" +
      runlatexLatexcgiURI +
			"\" method=\"post\" target=\"pre" + 0 +
			"ifr\"></form>";
    latexcgi('pre0');
}

function changecol(ele) {
	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);

	editor.session.setValue( keepchange(ele) );
	uppdf();
}

function showanswer() {
	var ele = ans1

	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);

	editor.session.setValue( keepchange(ele) );
	uppdf();
}

function showanswer2() {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var date = document.getElementById("dueDate").value;
	var chkdate = document.getElementById("ckdueDate").checked;

	var pro = wkst;
	var ele = ans2;

	//Edit ace editor source code
	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	//newtitle = newtitle.replace(/\s/g, '');
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(date != "") {
		date = "\\head{AGS Worksheet Generator}{Due Date: " + date + "}";
		newfront = newfront.replace("\\head{AGS Worksheet Generator}{Due Date: MM/DD/YYYY}", date);
	}

	if(chkdate == false) {
		newfront = newfront.replace(date, "\\head{AGS Worksheet Generator}{}");
	}

	editor.session.setValue(newfront + changecolrow(newcol, newrow, pro) + Newchangecolrow(newcol, newrow, ele) + backtex);
	uppdf();
}

function updatedpdf( ele ) {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var date = document.getElementById("dueDate").value;
	var chkdate = document.getElementById("ckdueDate").checked;

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(date != "") {
		date = "\\head{AGS Worksheet Generator}{Due Date: " + date + "}";
		newfront = newfront.replace("\\head{AGS Worksheet Generator}{Due Date: MM/DD/YYYY}", date);
	}

	if(chkdate == false) {
		newfront = newfront.replace(date, "\\head{AGS Worksheet Generator}{}");
	}

	document.getElementById("pretag").innerHTML = "<pre>" + newfront + changecolrow(newcol, newrow, ele) + backtex + "</pre>";
}

function exampleupdate(ex) {
	document.getElementById("pretag").innerHTML = "<pre>" + fronttex + getexample(ex) + "\\end{document}" + "</pre>";
}

function mainPDFdesign() {
	document.getElementById("pretag").innerHTML = "<pre>" + mainTex + "</pre>";
}



function changecolrow(c, r, e) {
	var final_e = ""
	for(let i = 0; i < e.length; i++) {
		var display = document.getElementById("display" + (i+1)).checked;
		var num = document.getElementById("numbers" + (i+1)).checked;
		var ckpnt = document.getElementById("ckpoints" + (i+1)).checked;
		var pnt = document.getElementById("points" + (i+1)).value;
		var desc = document.getElementById("subpdfdesc" + (i+1)).value;

		if(display == true) {
			if(num == true && ckpnt == true) {
				final_e += "\\pointproblem{" + parseInt(pnt) + "} " + desc + " \\vspace{0.5cm} \\par"
			}
			else if(num == false && ckpnt == true) {
				final_e += "\\pointprob{" + parseInt(pnt) + "} " + desc + " \\vspace{0.5cm} \\par"
			}
			else if(num == true && ckpnt == false) {
				final_e += "\\problem " + desc + " \\vspace{0.5cm} \\par"
			}
			else {
				final_e += "\\prob " + desc + "\\vspace{0.5cm} \\par"
			}

		final_e += '\\begin{tasks}[style=enumerate](' + c + ')';
		} else {
			if(i != 0) {
				final_e = final_e.substring(0, final_e.length - 23);
			} else {
				final_e += '\\begin{tasks}[style=enumerate](' + c + ')';
			}
		}
		final_e += e[i] + '\\end{tasks}\\vspace{3cm}'
	}
	return final_e;
}

function Newchangecolrow(c, r, e) {
	var pro = '\\newpage \\head{AGS Worksheet Generator}{Due Date: MM/DD/YYYY} \\ans This is the example sentence. \\vspace{0.5cm}';
	var newcol = '\\begin{tasks}[style=enumerate](' + c + ')';
	e = pro + newcol  + e + '\\end{tasks}\\vspace{3cm} \n '
	return e;
}
