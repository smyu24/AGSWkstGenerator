function keepchange(ele) {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var instrun = document.getElementById("pdfdesc").value;
	var date = document.getElementById("dueDate").value;

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	newtitle = newtitle.replace(/\s/g, '');
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(instrun != "") {
		instrun = "\\textbf{Instructions:} \\par \\noindent " + instrun + "\\pspace";
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", instrun);
	} else {
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", "");
	}

	if(date != "") {
	date = "\\head{MMTprep Worksheet}{Due Date: : " + date + "}";
	newfront = newfront.replace("\\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY}", date);
	} else {
		newfront = newfront.replace("\\textbf{#2} & & \\\\", "");
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

function changecol() {
	var ele = document.getElementById("seed").value;

	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);
	editor.session.setValue(keepchange(ele));
	uppdf();
}

function showanswer() {
	var ele = document.getElementById("answ").value;

	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);
	editor.session.setValue(keepchange(ele));
	uppdf();
}

function showanswer2() {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var instrun = document.getElementById("pdfdesc").value;
	var date = document.getElementById("dueDate").value;

	var pro = document.getElementById("seed").value;
	var ele = document.getElementById("Nansw").value;

	//Edit ace editor source code	
	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	newtitle = newtitle.replace(/\s/g, '');
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(instrun != "") {
		instrun = "\\textbf{Instructions:} \\par \\noindent " + instrun + "\\pspace";
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", instrun);
	} else {
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", "");
	}

	if(date != "") {
		date = "\\head{MMTprep Worksheet}{Due Date: : " + date + "}";
		newfront = newfront.replace("\\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY}", date);
	} else {
		newfront = newfront.replace("\\textbf{#2} & & \\\\", "");
	}

	editor.session.setValue(newfront + changecolrow(newcol, newrow, pro) + Newchangecolrow(newcol, newrow, ele) + backtex);
	uppdf();
}

function updatedpdf() {
	var newcol = parseInt(document.getElementById("numcol").value);
	var newrow = parseInt(document.getElementById("numrow").value);
	var newtitle = document.getElementById("pdftitle").value;
	var instrun = document.getElementById("pdfdesc").value;

	var ele = document.getElementById("seed").value;

	newtitle = "\\newcommand{\\term}{" + newtitle + "}";
	newtitle = newtitle.replace(/\s/g, '');
	var newfront = fronttex.replace("\\newcommand{\\term}{Worksheet Title}", newtitle);

	if(instrun != "") {
		instrun = "\\textbf{Instructions:} \\par \\noindent " + instrun + "\\pspace";
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", instrun);
	} else {
		newfront = newfront.replace("\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace", "");
	}

	document.getElementById("pretag").innerHTML = "<pre>" + newfront + changecolrow(newcol, newrow, ele) + backtex + "</pre>";
}

function exampleupdate(ex) {
	document.getElementById("pretag").innerHTML = "<pre>" + exfront + getexample(ex) + backtex + "</pre>";
}

function mainPDFdesign() {
	document.getElementById("pretag").innerHTML = "<pre>" + mainTex + "</pre>";
}