## 1.2.3 Finding Patterns In Geometric Shapes

#Growing, growing Dots

"""
# # Latex setup code

# \documentclass{article}
# \usepackage{tikz}

# \usetikzlibrary{math}

# \usepackage{environ}
# \makeatletter
# \newsavebox{\measure@tikzpicture}
# \NewEnviron{scaletikzpicturetowidth}[1]{%
#   \def\tikz@width{#1}%
#   \def\tikzscale{1}\begin{lrbox}{\measure@tikzpicture}%
#   \BODY
#   \end{lrbox}%
#   \pgfmathparse{#1/\wd\measure@tikzpicture}%
#   \edef\tikzscale{\pgfmathresult}%
#   \BODY
# }
# \makeatother



# % arg1 = diff
# % arg2 = zero term
# % arg3 = start fig
# % arg4 = end fig
# % arg5 = fig spacing
# \newcommand{\dotPattern}[5]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \foreach \step in {#3,...,#4}
#     {
#         \tikzmath{
#         \xmax = #1*\step + #2;
#         \y = (#4 - \step)*#5;
#         }
#         \foreach \x in {1,...,\xmax}
#             \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = arm growth (1/2 of diff)
# % arg2 = zero term
# % arg3 = start fig
# % arg4 = end fig
# % arg5 = fig spacing
# \newcommand{\wideLdotPattern}[5]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \foreach \step in {#3,...,#4}
#     {
#         \tikzmath{
#         \arm = #2 - 1 + #1*\step;
#         \xstart = 1 + (\step-1)*(#2 + #5 + #1*\step/2);
#         }
#         \foreach \block in {0,...,\arm}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \fill[red!50] (\x,1) ellipse (5pt and 4pt);
#         }
#         \tikzmath{\ymax = #1*\step + 1;}
#         \foreach \y in {2,...,\ymax}
#             \fill[red!50] (\xstart,\y) ellipse (5pt and 4pt);
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = arm growth (1/3 of diff)
# % arg2 = zero term
# % arg3 = start fig
# % arg4 = end fig
# % arg5 = fig spacing
# \newcommand{\tallLdotPattern}[5]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \foreach \step in {#3,...,#4}
#     {
#         \tikzmath{
#         \arm = #1*\step;
#         \xstart = \step + (\step-1)*(#5 + #1*\step/2);
#         }
#         \foreach \block in {0,...,\arm}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \fill[red!50] (\x,1) ellipse (5pt and 4pt);
#         }
#         \tikzmath{\ymax = \arm + #2;}
#         \foreach \y in {2,...,\ymax}
#             \fill[red!50] (\xstart,\y) ellipse (5pt and 4pt);
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = arm growth (1/3 of diff)
# % arg2 = zero term (must be odd)
# % arg3 = start fig
# % arg4 = end fig
# % arg5 = fig spacing
# \newcommand{\wideTdotPattern}[5]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \tikzmath{\halfFirst = (#2-1)/2;}
#     \foreach \step in {#3,...,#4}
#     {
#         \tikzmath{
#         \arm = #1*\step + \halfFirst;
#         \xmid = \halfFirst + #1*\step^2 + #5*\step + (\step-1)*#2;
#         \xstart = \xmid - \arm;
#         \basesteps = 2*\arm;
#         }
#         \foreach \block in {0,...,\basesteps}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \fill[red!50] (\x,1) ellipse (5pt and 4pt);
#         }
#         \tikzmath{\ymax = \arm - \halfFirst + 1;}
#         \foreach \y in {2,...,\ymax}
#             \fill[red!50] (\xmid,\y) ellipse (5pt and 4pt);
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = arm growth (1/3 of diff)
# % arg2 = zero term
# % arg3 = start fig
# % arg4 = end fig
# % arg5 = fig spacing
# \newcommand{\tallTdotPattern}[5]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \foreach \step in {#3,...,#4}
#     {
#         \tikzmath{
#         \arm = #1*\step;
#         \xmid = #1*\step^2 + \step + (\step-1)*#5;
#         \xstart = \xmid - \arm;
#         \basesteps = 2*\arm;
#         }
#         \foreach \block in {0,...,\basesteps}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \fill[red!50] (\x,1) ellipse (5pt and 4pt);
#         }
#         \tikzmath{\ymax = \arm + #2;}
#         \foreach \y in {2,...,\ymax}
#             \fill[red!50] (\xmid,\y) ellipse (5pt and 4pt);
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = width growth
# % arg2 = length growth
# % arg3 = zero term
# % arg4 = start fig
# % arg5 = end fig
# % arg6 = fig spacing
# \newcommand{\polyRectanglePattern}[6]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \foreach \step in {#4,...,#5}
#     {
#         \tikzmath{
#         \length = #2*\step + 1;
#         \width = #1*\step + #3 - 1;
#         \xstart = 1 + (\step-1)*(#3 + #6 + 1 + #1*\step/2);
#         }
#         \foreach \block in {0,...,\width}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \foreach \y in {1,...,\length}
#                 \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
#         }
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }

# % arg1 = length factor
# % arg2 = width factor
# % arg3 = zero term
# % arg4 = start fig
# % arg5 = end fig
# % arg6 = fig spacing
# \newcommand{\expRectanglePattern}[6]
# {\begin{scaletikzpicturetowidth}{0.5\textwidth}
# \begin{tikzpicture}[scale=\tikzscale]
#     \tikzmath{\width = #3 - 1;}
#     \foreach \step in {#4,...,#5}
#     {
#         \tikzmath{\length = #1^\step;}
#         \ifnum #2=1
#             \tikzmath{\xstart = 1 + (\step-1)*(\width + #6);}
#         \else
#             \tikzmath{
#             \width = #3*#2^\step - 1;
#             \xstart = 1 + #6*(\step-1) + (#3*#2 - \width + 1)/(1-#2);
#             }
#         \fi
#         \foreach \block in {0,...,\width}
#         {
#             \tikzmath{\x = \xstart + \block;}
#             \foreach \y in {1,...,\length}
#                 \fill[red!50] (\x,\y) ellipse (5pt and 4pt);
#         }
#     }
# \end{tikzpicture}
# \end{scaletikzpicturetowidth}
# }












# \begin{document}


# \noindent Example 1
# \\

# \dotPattern{2}{1}{1}{4}{1}

# \vspace{2cm}


# \noindent Example 2
# \\

# \wideTdotPattern{2}{3}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 3
# \\

# \tallTdotPattern{2}{3}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 4
# \\

# \wideLdotPattern{2}{3}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 5
# \\

# \tallLdotPattern{2}{3}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 6
# \\

# %linear
# \polyRectanglePattern{0}{1}{3}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 8
# \\

# %doubling
# \expRectanglePattern{2}{1}{5}{1}{3}{2}

# \vspace{2cm}


# \noindent Example 9 
# \\

# %quadrupling
# \expRectanglePattern{2}{2}{2}{1}{3}{2}



# \end{document}
"""


### Section 1:
#Draw Step 4 and Step 5.

# parameter will be a random selection from a static array
#of ["lin", "exp"]
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

