/**
 * PDF Creation
 */

function createpdf() {
	var element = document.getElementsByClassName("col-worksheet");

	for (var i = 0; i < element.length; i++) {
		element[i].style.display = "block";
	}

	var title = document.getElementById("dtitle").innerHTML;
	title = title.slice(3, -5);
	document.getElementById("txt-title").innerHTML = title;

	var sname = document.getElementById("sname").innerHTML;
	sname = sname.slice(3, -5);
	document.getElementById("txt-studnetName").innerHTML = sname;

	var seed = document.getElementById("dseed").innerHTML;
	seed = seed.slice(3, -5);
	seed = seed.replace(/<\/?span[^>]*>/g,"");
	seed = "\\(10\\overline{5} \\)"

	var divs = document.createElement('div');
	divs.innerHTML = seed;
	const typeset = document.querySelector('#wks-problems')
	typeset.appendChild(divs)
	setTimeout(function () {
		MathJax.typeset()
		typeset.appendChild(divs)
	  }, 10)

	  html2canvas(document.getElementsByClassName("wks-gen"), {
		onrendered: function(canvas) {
		  var imgData = canvas.toDataURL('image/png');
	
		  // Generate PDF
		  var doc = new jsPDF('p', 'pt', 'a4');
		  doc.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
		  doc.save('test.pdf');
		}
	  });

	//doc.save("output.pdf");
}