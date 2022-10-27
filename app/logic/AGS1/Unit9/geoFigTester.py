r"""
\begin{tikzpicture}
\coordinate [label=left:$A$] (A) at (-5,-5) {};
\coordinate [label=right:$B$] (B) at (5,-5) {};
\coordinate [label=right:$C$] (C) at (5,1) {};
\coordinate [label=left:$D$] (D) at (-5,1) {};

\draw [thick] (A) -- node[midway] {$\parallel$} (B) -- node[sloped]{$\parallel$} (C) -- (D) -- cycle;

\coordinate (S1) at ($(D)!0.66!(C)$);
\coordinate (S2) at ($(A)!0.11!(B)$);
\draw [very thick] (S1) -- node[above]{x} (S2);
\draw [red!100, thick] (S1) -- node[right]{T} (S1 |- S2);
\end{tikzpicture}
"""

class