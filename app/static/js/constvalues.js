/*
* This file is for saving the skeleton code of the worksheet.
*/

//This is the Latex code that has to be insert before calling the example problems.
const fronttex = `%!TeX pdf\n\\documentclass[11pt,letterpaper]{article}
\\usepackage[lmargin=1in,rmargin=1in,tmargin=1in,bmargin=1in]{geometry}
\\usepackage{amsmath,amssymb,enumerate,graphicx,lastpage,multicol,multirow,qrcode,stackengine,tikz,tasks,pgfplots}

\\usepackage[T1]{fontenc}
\\usepackage{charter}
\\usepackage[super]{nth}

\\everymath{\\displaystyle}

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

\\newcommand{\\prob}{\\noindent\\textbf{Problem. }}
\\newcounter{problem}
\\newcommand{\\problem}{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem. }%
}
\\newcommand{\\pointproblem}[1]{
	\\stepcounter{problem}%
	\\noindent \\textbf{Problem \\theproblem.} (#1 points)\\,%
}
\\newcommand{\\pointprob}[1]
    {\\noindent\\textbf{Problem. }(#1 points)\\,%
}
\\newcommand{\\point}[1]
    {\\noindent\\textbf{(#1 points)}\\,%
}

\\newcommand{\\pspace}{\\par\\vspace{\\baselineskip}}
\\newcommand{\\ds}{\\displaystyle}

\\settasks{after-item-skip=6em,
	after-skip=2cm,
	label-width=2em,
	item-indent=3em,
	label=\\arabic*),
	column-sep=2em
	}

\\usepackage{fancyhdr}


\\newcommand{\\drawaline}[4]{
\\draw [very thick, extended line=1cm,stealth-stealth] (#1,#2)--(#3,#4);
\\fill [black](#1,#2) circle(4pt);
\\fill [black](#3,#4) circle(4pt);
}

\\pgfplotsset{compat=1.17}
\\pgfmathsetseed{\\number\\pdfrandomseed}
\\newcommand{\\LinearEquation}[2]
{
\\pgfmathsetmacro{\\Slope}{(#1)}
\\pgfmathsetmacro{\\Intercept}{#2}

\\(y={\\Slope}x+\\Intercept\\)

\\begin{tikzpicture}[scale=0.3]
\\draw[help lines, gray, thin] (-10,-10) grid (10,10);
\\draw[very thick, black, <->] (-10.3,0)--(10.3,0);
\\draw[very thick, black, <->] (0,-10.3)--(0,10.3);
\\clip  (-10,-10) rectangle (10,10);
\\draw[red, very thick, domain=-10:10] plot (\\x,\\Slope*\\x+\\Intercept);
\\end{tikzpicture}
}

\\usepgfplotslibrary{fillbetween}
\\usetikzlibrary{patterns}

\\pgfplotsset{
     mmt axis style/.style={
         grid=both,
         grid style={line width=.1pt, draw=gray!20},
         major grid style={line width=.2pt,draw=gray!60},
         axis lines=middle,
         minor tick num=4,
         enlargelimits={abs=0.5},
         unit vector ratio*=1 1 1,
         axis line style={latex-latex},
         ticklabel style={font=\\scriptsize},
         xlabel=$x$,
         ylabel=$y$,
         xlabel style={at={(ticklabel* cs:1)},anchor=west},
         ylabel style={at={(ticklabel* cs:1)},anchor=south},
},}



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
\\head{AGS Worksheet Generator}{Due Date: MM/DD/YYYY}`;

//This is the code for the QR code
const backtex = `{\\raggedleft\\vfill\\itshape\\Longstack[l]{%
	\\quad
	/*\\qrcode{ PUT DYNAMIC URL HERE AND LINK TO ACTUAL DATA } */
	}\\par
}
\\end{document}`;