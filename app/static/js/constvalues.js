const mainTex = `%!TeX pdf\n\\documentclass[11pt,letterpaper]{article}
\\usepackage[lmargin=1in,rmargin=1in,tmargin=1in,bmargin=1in]{geometry}

\\usepackage{amsmath, amssymb, enumerate, graphicx, lastpage, multicol, multirow, qrcode, stackengine}

\\usepackage[T1]{fontenc}
\\usepackage{charter}

\\newcommand{\\class}{Section Title}
\\newcommand{\\term}{Worksheet Title}
\\newcommand{\\head}[2]{%
	\\thispagestyle{empty}
	\\vspace*{-0.5in}

	\\noindent\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}
	\\textbf{#1} & \\textbf{Name:} & \\makebox[8cm]{\\hrulefill} \\\\
	\\textbf{#2} & & \\\\
	\\textbf{\\class:\\; \\term} & & \\\\
	\\end{tabular*} \\\\
	\\rule[2ex]{\\textwidth}{2pt} %
}


\\newcommand{\\prob}{\\noindent\\textbf{Section. }}
\\newcounter{problem}
\\newcommand{\\problem}{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem. }%
}

\\newcommand{\\pointproblem}[1]{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem.} (#1 points)\\,%
}

\\newcommand{\\pspace}{\\par\\vspace{\\baselineskip}}
\\newcommand{\\ds}{\\displaystyle}

\\usepackage{fancyhdr}

\\fancypagestyle{pages}{
	\\fancyhead[L]{}
	\\fancyhead[C]{}
	\\fancyhead[R]{}
\\renewcommand{\\headrulewidth}{0pt}
	\\fancyfoot[L]{}
	\\fancyfoot[C]{}
	\\fancyfoot[R]{}
\\renewcommand{\\footrulewidth}{0.0pt}
}
\\headheight=0pt
\\footskip=14pt

\\pagestyle{pages}



\\begin{document}
\\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY}
\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace

\\pointproblem{5} This is the example document. \\vspace{1.5cm}

\\begin{multicols}{3}
\\begin{enumerate}
  \\item $13-x=-3$ \\vspace{2cm}
\\end{enumerate}
\\end{multicols}
\\vspace{3cm}


{\\raggedleft\\vfill\\itshape\\Longstack[l]{%
\\quad
\\qrcode{https://aiden1393.pythonanywhere.com/}
}\\par
}

\\end{document}`;

const fronttex = `%!TeX pdf\n\\documentclass[11pt,letterpaper]{article}
\\usepackage[lmargin=1in,rmargin=1in,tmargin=1in,bmargin=1in]{geometry}

\\usepackage{amsmath, amssymb, enumerate, graphicx, lastpage, multicol, multirow, qrcode, stackengine}

\\usepackage[T1]{fontenc}
\\usepackage{charter}

\\newcommand{\\class}{Section Title}
\\newcommand{\\term}{Worksheet Title}
\\newcommand{\\head}[2]{%
	\\thispagestyle{empty}
	\\vspace*{-0.5in}

	\\noindent\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}
	\\textbf{#1} & \\textbf{Name:} & \\makebox[8cm]{\\hrulefill} \\\\
	\\textbf{#2} & & \\\\
	\\textbf{\\class:\\; \\term} & & \\\\
	\\end{tabular*} \\\\
	\\rule[2ex]{\\textwidth}{2pt} %
}

\\newcommand{\\ans}{\\noindent\\textbf{Answer. }}

\\newcommand{\\prob}{\\noindent\\textbf{Section. }}
\\newcounter{problem}
\\newcommand{\\problem}{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem. }%
}

\\newcommand{\\pointproblem}[1]{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem.} (#1 points)\\,%
}

\\newcommand{\\pspace}{\\par\\vspace{\\baselineskip}}
\\newcommand{\\ds}{\\displaystyle}

\\usepackage{fancyhdr}

\\fancypagestyle{pages}{
	\\fancyhead[L]{}
	\\fancyhead[C]{}
	\\fancyhead[R]{}
\\renewcommand{\\headrulewidth}{0pt}
	\\fancyfoot[L]{}
	\\fancyfoot[C]{}
	\\fancyfoot[R]{}
\\renewcommand{\\footrulewidth}{0.0pt}
}
\\headheight=0pt
\\footskip=14pt

\\pagestyle{pages}

\\begin{document}
\\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY}
\\textbf{Instructions:} \\par \\noindent Here are the instructions \\pspace

\\pointproblem{5} This is the example sentence. \\vspace{0.5cm}`;

const backtex = `{\\raggedleft\\vfill\\itshape\\Longstack[l]{%
	\\quad
	\\qrcode{https://aiden1393.pythonanywhere.com/}
	}\\par
}
\\end{document}`;

const exfront = `%!TeX pdf\n\\documentclass[11pt,letterpaper]{article}
\\usepackage[lmargin=1in,rmargin=1in,tmargin=1in,bmargin=1in]{geometry}

\\usepackage{amsmath, amssymb, enumerate, graphicx, lastpage, multicol, multirow, qrcode, stackengine}

\\usepackage[T1]{fontenc}
\\usepackage{charter}

\\newcommand{\\class}{Section Title}
\\newcommand{\\term}{Worksheet Title}
\\newcommand{\\head}[2]{%
	\\thispagestyle{empty}
	\\vspace*{-0.5in}

	\\noindent\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}
	\\textbf{#1} & \\textbf{Name:} & \\makebox[8cm]{\\hrulefill} \\\\
	\\textbf{#2} & & \\\\
	\\textbf{\\class:\\; \\term} & & \\\\
	\\end{tabular*} \\\\
	\\rule[2ex]{\\textwidth}{2pt} %
}

\\newcommand{\\ans}{\\noindent\\textbf{Answer. }}

\\newcommand{\\prob}{\\noindent\\textbf{Section. }}
\\newcounter{problem}
\\newcommand{\\problem}{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem. }%
}

\\newcommand{\\pointproblem}[1]{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem.} (#1 points)\\,%
}

\\newcommand{\\pspace}{\\par\\vspace{\\baselineskip}}
\\newcommand{\\ds}{\\displaystyle}

\\usepackage{fancyhdr}

\\fancypagestyle{pages}{
	\\fancyhead[L]{}
	\\fancyhead[C]{}
	\\fancyhead[R]{}
\\renewcommand{\\headrulewidth}{0pt}
	\\fancyfoot[L]{}
	\\fancyfoot[C]{}
	\\fancyfoot[R]{}
\\renewcommand{\\footrulewidth}{0.0pt}
}
\\headheight=0pt
\\footskip=14pt

\\pagestyle{pages}

\\begin{document}
\\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY}`;


function changecolrow(c, r, e) {
	var newcol = '\\begin{multicols}{' + c + '}';
	e = newcol + '\\begin{enumerate}' + e + '\\end{enumerate}\\end{multicols}\\vspace{3cm}'
	
	newr = "\\vspace{" + r + "cm}";
	newr = newr.replace(/\s/g, '');
	
	e = e.replaceAll("\\vspace{2cm}", newr);
	return e;
}

function Newchangecolrow(c, r, e) {
	var pro = '\\newpage \\head{MMTprep Worksheet}{Due Date: MM/DD/YYYY} \\ans This is the example sentence. \\vspace{1.5cm}';
	var newcol = '\\begin{multicols}{' + c + '}';
	e = pro + newcol + '\\begin{enumerate}' + e + '\\end{enumerate}\\end{multicols}\\vspace{3cm}'
	return e;
}
