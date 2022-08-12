## 1.2.3 Finding Patterns In Geometric Shapes

#Growing, growing Dots
"""
\documentclass{article}
\usepackage{tikz}

\usetikzlibrary{math}

\usepackage{environ}
\makeatletter
\newsavebox{\measure@tikzpicture}
\NewEnviron{scaletikzpicturetowidth}[1]{%
  \def\tikz@width{#1}%
  \def\tikzscale{1}\begin{lrbox}{\measure@tikzpicture}%
  \BODY
  \end{lrbox}%
  \pgfmathparse{#1/\wd\measure@tikzpicture}%
  \edef\tikzscale{\pgfmathresult}%
  \BODY
}
\makeatother



% arg1 = diff
% arg2 = zero term
% arg3 = start fig
% arg4 = end fig
% arg5 = fig spacing
\newcommand{\dotPattern}[5]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \foreach \step in {#3,...,#4}
    {
        \tikzmath{
        \xmax = #1*\step + #2;
        \y = (#4 - \step)*#5;
        }
        \foreach \x in {1,...,\xmax}
            \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = arm growth (1/2 of diff)
% arg2 = zero term
% arg3 = start fig
% arg4 = end fig
% arg5 = fig spacing
\newcommand{\wideLdotPattern}[5]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \foreach \step in {#3,...,#4}
    {
        \tikzmath{
        \arm = #2 - 1 + #1*\step;
        \xstart = 1 + (\step-1)*(#2 + #5 + #1*\step/2);
        }
        \foreach \block in {0,...,\arm}
        {
            \tikzmath{\x = \xstart + \block;}
            \fill[red!50] (\x,1) ellipse (5pt and 4pt);
        }
        \tikzmath{\ymax = #1*\step + 1;}
        \foreach \y in {2,...,\ymax}
            \fill[red!50] (\xstart,\y) ellipse (5pt and 4pt);
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = arm growth (1/3 of diff)
% arg2 = zero term
% arg3 = start fig
% arg4 = end fig
% arg5 = fig spacing
\newcommand{\tallLdotPattern}[5]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \foreach \step in {#3,...,#4}
    {
        \tikzmath{
        \arm = #1*\step;
        \xstart = \step + (\step-1)*(#5 + #1*\step/2);
        }
        \foreach \block in {0,...,\arm}
        {
            \tikzmath{\x = \xstart + \block;}
            \fill[red!50] (\x,1) ellipse (5pt and 4pt);
        }
        \tikzmath{\ymax = \arm + #2;}
        \foreach \y in {2,...,\ymax}
            \fill[red!50] (\xstart,\y) ellipse (5pt and 4pt);
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = arm growth (1/3 of diff)
% arg2 = zero term (must be odd)
% arg3 = start fig
% arg4 = end fig
% arg5 = fig spacing
\newcommand{\wideTdotPattern}[5]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \tikzmath{\halfFirst = (#2-1)/2;}
    \foreach \step in {#3,...,#4}
    {
        \tikzmath{
        \arm = #1*\step + \halfFirst;
        \xmid = \halfFirst + #1*\step^2 + #5*\step + (\step-1)*#2;
        \xstart = \xmid - \arm;
        \basesteps = 2*\arm;
        }
        \foreach \block in {0,...,\basesteps}
        {
            \tikzmath{\x = \xstart + \block;}
            \fill[red!50] (\x,1) ellipse (5pt and 4pt);
        }
        \tikzmath{\ymax = \arm - \halfFirst + 1;}
        \foreach \y in {2,...,\ymax}
            \fill[red!50] (\xmid,\y) ellipse (5pt and 4pt);
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = arm growth (1/3 of diff)
% arg2 = zero term
% arg3 = start fig
% arg4 = end fig
% arg5 = fig spacing
\newcommand{\tallTdotPattern}[5]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \foreach \step in {#3,...,#4}
    {
        \tikzmath{
        \arm = #1*\step;
        \xmid = #1*\step^2 + \step + (\step-1)*#5;
        \xstart = \xmid - \arm;
        \basesteps = 2*\arm;
        }
        \foreach \block in {0,...,\basesteps}
        {
            \tikzmath{\x = \xstart + \block;}
            \fill[red!50] (\x,1) circle (10pt);
        }
        \tikzmath{\ymax = \arm + #2;}
        \foreach \y in {2,...,\ymax}
            \fill[red!50] (\xmid,\y) circle (10pt);
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = width growth
% arg2 = length growth
% arg3 = zero term
% arg4 = start fig
% arg5 = end fig
% arg6 = fig spacing
\newcommand{\polyRectanglePattern}[6]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \foreach \step in {#4,...,#5}
    {
        \tikzmath{
        \length = #2*\step + 1;
        \width = #1*\step + #3 - 1;
        \xstart = 1 + (\step-1)*(#3 + #6 + 1 + #1*\step/2);
        }
        \foreach \block in {0,...,\width}
        {
            \tikzmath{\x = \xstart + \block;}
            \foreach \y in {1,...,\length}
                \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
        }
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = length factor
% arg2 = width factor
% arg3 = zero term
% arg4 = start fig
% arg5 = end fig
% arg6 = fig spacing
\newcommand{\expRectanglePattern}[6]
{\begin{scaletikzpicturetowidth}{0.5\textwidth}
\begin{tikzpicture}[scale=\tikzscale]
    \tikzmath{\width = #3 - 1;}
    \foreach \step in {#4,...,#5}
    {
        \tikzmath{\length = #1^\step;}
        \ifnum #2=1
            \tikzmath{\xstart = 1 + (\step-1)*(\width + #6);}
        \else
            \tikzmath{
            \width = #3*#2^\step - 1;
            \xstart = 1 + #6*(\step-1) + (#3*#2 - \width + 1)/(1-#2);
            }
        \fi
        \foreach \block in {0,...,\width}
        {
            \tikzmath{\x = \xstart + \block;}
            \foreach \y in {1,...,\length}
                \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
        }
    }
\end{tikzpicture}
\end{scaletikzpicturetowidth}
}

% arg1 = growth
% arg2 = start
% arg3 = number of figs
\newcommand{\boxPattern}[3]
{\foreach \step in {1,...,#3}
{   
    \begin{tikzpicture}
        \draw {(0,0)--(1,0)};
        \tikzmath{\height = #2 + #1*\step;}
        \foreach \square in {1,...,\height} 
        {
            \draw {(0,\square-1)--(0,\square)--(1,\square)--(1,\square-1)};
        }
    \end{tikzpicture}
    \qquad
}
}

% arg1 = growth
% arg2 = start
% arg3 = number of figs
\newcommand{\stairPattern}[3]
{\foreach \step in {1,...,#3}
{   
    \begin{tikzpicture}
        \tikzmath{\height = #2 + #1*\step;}
        \foreach \y in {1,...,\height}
        {   
            \draw {(\y-1,0)--(\y,0)};
            \foreach \square in {1,...,\y} 
            {
                \draw {(\y-1,\square-1)--(\y-1,\square)--(\y,\square)--(\y,\square-1)};
            }
        }
    \end{tikzpicture}
    \qquad
}
}












\begin{document}




\tallTdotPattern{4}{3}{1}{3}{2}

\tallTdotPattern{4}{3}{4}{5}{2}

\tallTdotPattern{4}{-1}{1}{3}{2}

\tallTdotPattern{4}{-1}{4}{5}{2}

\tallLdotPattern{4}{0}{1}{3}{2}

\tallLdotPattern{4}{0}{4}{5}{2}

\tallTdotPattern{2}{0}{1}{3}{2}

\tallTdotPattern{2}{0}{4}{5}{2}

\wideLdotPattern{4}{-1}{1}{3}{2}

\wideLdotPattern{4}{-1}{4}{5}{2}

\wideLdotPattern{4}{0}{1}{3}{2}

\wideLdotPattern{4}{0}{4}{5}{2}

\tallLdotPattern{2}{-1}{1}{3}{2}

\tallLdotPattern{2}{-1}{4}{5}{2}

\dotPattern{1}{0}{1}{3}{2}

\dotPattern{1}{0}{4}{5}{2}

\dotPattern{1}{0}{1}{3}{2}

\dotPattern{1}{0}{4}{5}{2}

\polyRectanglePattern{0}{3}{0}{1}{3}{2}

\polyRectanglePattern{0}{3}{0}{4}{5}{2}












% \noindent Example 1
% \\

% \begin{tikzpicture}
%   \foreach \x in {1,3,...,7}
%     \foreach \y in {1,...,8}
%     {
%       \fill[red!50] (\x,\y) ellipse (3pt and 6pt);
%       \ifnum \x<\y
%         \breakforeach
%       \fi
%     }
% \end{tikzpicture}

% \vspace{2cm}


% \noindent Example 2
% \\

% \tikz
%   \draw (0,0)
%     \foreach \x in {1}
%       { -- (\x,1) -- (\x,0) };
%     \qquad
% \tikz
%   \draw (0,0)
%     \foreach \x in {1,2}
%       { -- (\x,1) -- (\x,0) };
%     \qquad
% \tikz
%   \draw (0,0)
%     \foreach \x in {1,2,3}
%       { -- (\x,1) -- (\x,0) };

% \vspace{2cm}


% \noindent Example 3
% \\

% \tikz \draw(0,0)  \foreach \p in {1,2} {(\p,1)--(\p,3) (1,\p)--(3,\p)};
% \qquad
% \tikz \draw(0,0) \foreach \p in {1,2,3} {(\p,1)--(\p,3) (1,\p)--(3,\p)};
% \qquad
% \tikz \draw(0,0) \foreach \p in {1,2,3,4} {(\p,1)--(\p,3) (1,\p)--(3,\p)};
% \qquad

% \vspace{2cm}


% \noindent Example 4
% \\

% \dotPattern{2}{1}{4}

% \vspace{2cm}


% \noindent Example 5
% \\

% \wideTdotPattern{2}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 6
% \\

% \tallTdotPattern{2}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 7
% \\

% \wideLdotPattern{2}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 8
% \\

% \tallLdotPattern{2}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 9
% \\

% %linear
% \polyRectanglePattern{0}{1}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 10
% \\

% %quadratic
% \polyRectanglePattern{1}{2}{3}{3}{2}

% \vspace{2cm}


% \noindent Example 11
% \\

% %doubling
% \expRectanglePattern{2}{1}{5}{3}{2}

% \vspace{2cm}


% \noindent Example 12
% \\

% %quadrupling
% \expRectanglePattern{2}{2}{2}{3}{2}

% \vspace{2cm}


% \noindent Example 13
% \\

% \boxPattern{2}{3}{5}

% \vspace{2cm}


% \noindent Example 14
% \\

% \stairPattern{2}{2}{3}

% \vspace{2cm}



%\begin{tikzpicture}
%\foreach \i in {1,...,3}{
%    \foreach \j in {1,...,3}{
%        \shade[ball color = orange] (\i,\j) circle (0.25);
%    }
%}
%\end{tikzpicture}
%\pgfmathsetmacro{\n}{5}
%\pgfmathtruncatemacro{\nodes}{\n -1}
%\node[fill,circle,draw] (c) at (0,0) {};
%\foreach \i in {0 ,... ,\nodes }
%\node [fill , circle ,draw] (\i) at (90+\i *360/\n :1) {};
%\foreach \i in {0 ,... ,\nodes } {
%\draw [ red ] ( c ) to (\i);
%\pgfmathtruncatemacro {\j}{ mod ( round (1+\ i) ,\ n )}
%\draw [ red ] (\i) -- (\j);
%}
\end{document}
"""

# parameter will be a random selection from a static array
#of ["lin", "exp"]

import sys; sys.path.insert(0, "..")

from loader import ArithSeq, brackify, GeoSeq
from sympy import *
from random import randint


def Finding_Patterns_In_Geometric_Shapes(kind='lin'):
    if kind == 'lin':
        case = randint(1,6)
        growth, intercept = [randint(1,4),randint(-1,3)]
        if case == 1: # line of dots
            diff = growth
            problem, answer = [r'\dotPattern']*2
        elif case in [2,3]: # wide  or tall L
            diff = 2*growth
            problem, answer = [r'\wideLdotPattern']*2 if case==2 else [r'\tallLdotPattern']*2
        elif case in [4,5]: # wide or tall T
            diff = 3*growth
            problem, answer = [r'\wideTdotPattern']*2 if case==4 else [r'\tallTdotPattern']*2
        elif case == 6: # rectangle
            diff = intercept*growth
            problem, answer = [r'\polyRectanglePattern{0}']*2

        seq = ArithSeq(diff, intercept)
        problem += brackify(growth) + brackify(intercept) + '{1}{3}{2}'
        answer += brackify(growth) + brackify(intercept) + '{4}{5}{2}'
    elif kind == 'exp':
        growth1, growth2 = randint(2,3), randint(1,2)
        seq = GeoSeq(growth1*growth2, randint(2,3))
        problem, answer = [r'\expRectanglePattern']*2
        problem += brackify(growth1) + brackify(growth2) + brackify(seq.intercept) + '{1}{3}{2}'
        answer += brackify(growth1) + brackify(growth2) + brackify(seq.intercept) + '{4}{5}{2}'

    return problem, answer

