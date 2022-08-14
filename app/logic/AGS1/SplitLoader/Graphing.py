from Imports import *
from PrintingFunctions import signify, brackify, latexify
from Generators import getInt

def startGraph(xmin=-10,xmax=10,ymin=-10,ymax=10):
    xstart = 5*(xmin//5)
    ystart = 5*(ymin//5)
    xtick = brackify(f'{xstart},{xstart+5},...,{xmax+5}')
    ytick = brackify(f'{ystart},{ystart+5},...,{ymax+5}')

    tex = r'\begin{tikzpicture}\begin{axis}[mmt axis style,'
    tex += fr'xmin={xmin},xmax={xmax},xtick={xtick},ymin={ymin},ymax={ymax},ytick={ytick},]'
    return tex

def endGraph():
    return r'\end{axis}\end{tikzpicture}'

def emptyGraph(xmin=-10,xmax=10,ymin=-10,ymax=10):
    return startGraph(xmin,xmax,ymin,ymax) + endGraph()

def drawPt(pt, draw='black', fill='black', shape='circle', size='2pt', label=None):
    string = fr'\fill[draw={draw},fill={fill}] (axis cs: {pt[0]},{pt[1]}) {shape}({size})'

    if label==None:
        return string + r';'
    else:
        if type(label) != list:
            label = [label, 'above right']
        return string + fr' node[{label[1]}] {brackify(signify(label[0]))};'

def drawScatter(pts, draw='black', fill='black', shape='', size='2pt'):
    """
    Return LaTeX to draw list of points on a graph.

    Parameters
    ----------
        pts : list
            List of coordinate pairs.
        draw : string, default='black'
            Color of mark boundaries.
        fill : string, default='black'
            Color of mark fills.
        shape : string, default=''
            Shape of marks, default='' gives circle.
                Other options include 'triangle','square','diamond,'star','otimes'.
        size : string, default='2pt'
    """

    pts = ' '.join([str(tuple(jj)) for jj in pts])
    return fr'\addplot[only marks,draw={draw},fill={fill},mark={shape}*,mark size={size}] coordinates {brackify(pts)};'

def getGraphBounds(coords):
    xmin, xmax = min(-10,*[5*(jj[0]//5) for jj in coords]), max(10,*[5*(jj[0]//5+1) for jj in coords])
    ymin, ymax = min(-10,*[5*(jj[1]//5) for jj in coords]), max(10,*[5*(jj[1]//5+1) for jj in coords])

    return xmin, xmax, ymin, ymax

def drawLinear(expr,xmin,xmax,color='black',style='solid'):
    string = fr'\addplot[{style},domain={xmin}:{xmax}, color={color},]{brackify(expr)};'
    return string

def drawCurve(expr, inMin, inMax, LHS='y', color='black', style='solid', width='thick', label=None, fillName=None):
    """
    Return LaTeX to draw a curve on a graph.

    Parameters
    ----------
        expr : string or sympy expression
            Right-hand side of equation
        inMin : number
            Minimum value of independent variable.
        inMax : number
            Maximum value of independent variable.
        LHS : string, default='y'
            Left-hand side of equation.
        color : string, default='black'
        style : string, default='solid'
        width : string, default='thick'
        label : list or string, default=None
            If list, format as [<label>, <rel. pos.>, <angle>] where rel. pos.
                is relative position as a float in [0,1] and angle is given in degrees.
            If string, default rel. pos.=0.7 and default angle=45.
        fillName : string, default=None
            Name of curve used for fillbetween library (needed only for inequality graphers).
    """
    
    string = fr'\addplot[{color},{style},{width},domain={inMin}:{inMax},samples=100'
    string += r'] ' if fillName==None else fr',name path={fillName}] '

    variables = sympify(expr).free_symbols
    expr = str(expr).replace('**','^')

    if (variables=={x}) or (LHS in ['y',y]):        # Function of x
        string += brackify(expr)
    elif (variables=={y}) or (LHS in ['x',x]):      # Function of y
        expr = expr.replace('y','x')
        string += f'({brackify(expr)},{brackify(x)})'

    if label==None:
        return string + r';'
    else:
        if type(label) != list:
            label = [label, 0.7, 45]
        return string + fr' node[pos={label[1]},pin={label[2]}:{signify(label[0])}]' + r' {};'

def drawSlopeTri(pt1, pt2):
    string = fr'\draw[dashed] (axis cs: {pt1[0]},{pt1[1]}) -- (axis cs: {pt1[0]},{pt2[1]});'
    string += fr'\draw[dashed] (axis cs: {pt1[0]},{pt2[1]}) -- (axis cs: {pt2[0]},{pt2[1]});'
    return string

def shadeRegion(xmin, xmax, lower, upper, color='blue!30', shading='opacity=0.5'):
    domain = fr'domain={xmin}:{xmax}'
    string = fr'\addplot[{color},{shading}] fill between'
    string += fr'[of={lower} and {upper},soft clip={brackify(domain)}];'
    return string

def scaleTikz(string, width=0.25):
    start = r'\begin{scaletikzpicturetowidth}{' + str(width) + r'\textwidth}'
    end = r'\end{scaletikzpicturetowidth}'
    string = string.replace(r'\begin{tikzpicture}',r'\begin{tikzpicture}[scale=\tikzscale]')

    return start + string + end

def startNumLine(xmin=-10,xmax=10):
    xstart = 5*(xmin//5)
    xtick = brackify(f'{xstart},{xstart+5},...,{xmax+5}')

    string = r'\begin{tikzpicture}\begin{axis}[mmt numline style,'
    string += fr'xmin={xmin},xmax={xmax},xtick={xtick}]'
    return string

def endNumLine():
    return r'\end{axis}\end{tikzpicture}'

def drawInterval(interval, color='red', thickness='ultra thick', style='-'):
    string = fr'\addplot[{color},{thickness},{style},domain={interval.start}:{interval.end}] {brackify(0)};'
    return string

def emptyNumLine(xmin=-10,xmax=10):
    return startNumLine(xmin,xmax) + endNumLine()

def graphSet(realset, xmin=None,xmax=None):
    """
    Return LaTeX for real set displayed on the real line.

    Parameters
    ----------
        realset : sympy Set
    """

    endpts = list(realset.boundary)

    if len(endpts) == 0:
        xmin = -11 if xmin==None else xmin
        xmax = 11 if xmax==None else xmax
        graph = startNumLine(xmin,xmax)
        graph += drawInterval(Interval(xmin,xmax), style='latex-latex') if realset!=EmptySet else ''
    else:
        xmin = 5*(min(endpts)//5)-1 if xmin==None else xmin
        xmax = 5*(max(endpts)//5)+6 if xmax==None else xmax
        graph = startNumLine(xmin,xmax)

        if (min(endpts)-1) in realset:
            graph += drawInterval(Interval(xmin,min(endpts)), style='latex-')
        for count,jj in enumerate(endpts[:-1]):
            if (jj+endpts[count+1])/2 in realset:
                graph += drawInterval(Interval(jj,endpts[count+1]))
        if (max(endpts)+1) in realset:
            graph += drawInterval(Interval(max(endpts),xmax), style='-latex')

    for jj in endpts:
        fill = 'black' if jj in realset else 'white'
        graph += drawPt([jj,0],fill=fill)

    graph += endNumLine()

    return graph

def graphInequals(*inequals, compound='and', xmin=None, xmax=None, variable=x):
    """
    Return LaTeX for solutions of inequalities displayed on the real line.

    Parameters
    ----------
        inequals : array of inequality lists
            Enter inequalities as [expr, rel] if polynomial or [numer, denom, rel] if rational, RHS always assumed zero.
        compound : str, default='and'
            Compound inequality type; AND='and', 'n', or 'intersection; OR='or', 'u', or 'union'
    """

    inequals = [[jj[0],1,jj[1]] if len(jj)==2 else jj for jj in inequals]
    inequals = [(( Poly(sympify(jj[0]),variable), Poly(sympify(jj[1]),variable) ), jj[2]) for jj in inequals]

    if compound in ['and','n','intersection']:
        solutions = solve_rational_inequalities([inequals])
    elif compound in ['or','u','union']:
        solutions = EmptySet
        for jj in inequals:
            solutions = solutions.union(solve_rational_inequalities([[jj]]))

    return graphSet(solutions,xmin,xmax), solutions

def graphInequal2D(rel, expr, xmin=-10, xmax=10, ymin=-10, ymax=10, color='blue!30', shading='opacity=0.5'):
    """
    Return LaTeX for two variable inequality.

    Parameters
    ----------
        rel : relational string
            Must be '>','>=','=>',r'\geq ','<','<=','=<',r'\leq ', or any of these preceded by 'x' or 'y'.
        expr : sympy expression
            RHS of inequality, LHS assumed y unless includled in relation.
    """
    
    aboves, belows = {'>','>=','=>',r'\geq '}, {'<','<=','=<',r'\leq '}

    graph = startGraph(xmin, xmax, ymin, ymax)
    xmin, xmax, ymin, ymax = xmin-5, xmax+5, ymin-5, ymax+5

    # Check for vertical boundary
    rel = rel.replace('y','')
    if 'x' in rel:
        inMin, inMax, LHS = ymin, ymax, 'x'
        left, right = [expr, xmax] if (rel.replace('x','') in aboves) else [xmin, expr]
    else:
        inMin, inMax, LHS = xmin, xmax, 'y'
        left, right = inMin, inMax

    # Draw boundary
    style = 'solid' if (('=' in rel) or ('eq' in rel)) else 'dashed'
    graph += drawCurve(expr, inMin, inMax, LHS=LHS, style=style, fillName='f')

    # Make upper and/or lower boundaries
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=top] {brackify(ymax+5)};'
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=bottom] {brackify(ymin-5)};'
    if rel in aboves:
        upper, lower = 'top', 'f'
    elif rel in belows:
        upper, lower = 'f', 'bottom'
    else:
        upper, lower = 'top','bottom'

    # Shade region
    graph += shadeRegion(left, right, lower, upper, color=color, shading=shading)
    
    graph += endGraph()

    return graph

def graphSysInequals2D(rel1, expr1, rel2, expr2, xmin=-10, xmax=10, ymin=-10, ymax=10, color='blue!30', shading='opacity=0.5'):
    """
    Return LaTeX for system of inequalities graph.

    Parameters
    ----------
        rel1 : relational string
            Must be '>','>=','=>',r'\geq ','<','<=','=<',r'\leq ', or any of these preceded by 'x' or 'y'.
        expr1 : sympy expression
            RHS of inequality, LHS assumed y unless included in relation.
        rel2 : relational string
        expr2 : sympy expression
    """

    aboves, belows = {'>','>=','=>',r'\geq '}, {'<','<=','=<',r'\leq '}

    graph = startGraph(xmin, xmax, ymin, ymax)
    xmin, xmax, ymin, ymax = xmin-5, xmax+5, ymin-5, ymax+5

    # Check and set up for vertical boundaries
    rel1, rel2 = rel1.replace('y',''), rel2.replace('y','')
    xrel1, xrel2 = rel1.replace('x',''), rel2.replace('x','')
    LHS1, LHS2 = (y if rel1==xrel1 else x), (y if rel2==xrel2 else x)
    inMin1, inMax1 = [xmin, xmax] if LHS1==y else [ymin, ymax]
    inMin2, inMax2 = [xmin, xmax] if LHS2==y else [ymin, ymax]

    # Set endpoints for shading
    if (LHS1==x) and (LHS2==x):     # Both vertical
        if {xrel1,xrel2}.issubset(aboves) or {xrel1,xrel2}.issubset(belows):                    # Both right or both left
            endpts = {xmax}.union({max(expr1,expr2)}) if xrel1 in aboves else {xmin}.union({min(expr1,expr2)})
        elif ((xrel1 in aboves) and (expr1<expr2)) or ((xrel1 in belows) and (expr1>expr2)):    # Between verticals
            endpts = {expr1,expr2}
        else:                                                                                   # No overlap
            endpts = {xmax}
    elif LHS1 == x:                 # One vertical
        endpts = {expr1,xmax} if xrel1 in aboves else {xmin,expr1}
    elif LHS2 == x:                 # One vertical
        endpts = {expr2,xmax} if xrel2 in aboves else {xmin,expr2}
    else:                           # Split at intersections if no vertical boundaries
        intersects = solve([y-expr1, y-expr2], dict=True)
        endpts = {jj[x] for jj in intersects if jj[x] in Interval(xmin,xmax)}
        endpts = endpts.union({xmin,xmax})
    endpts = sorted(endpts)
    
    # Draw boundaries
    style1 = 'solid' if (('=' in rel1) or ('eq' in rel1)) else 'dashed'
    style2 = 'solid' if (('=' in rel2) or ('eq' in rel2)) else 'dashed'
    graph += drawCurve(expr1, inMin1, inMax1, LHS=LHS1, style=style1, fillName='f1')
    graph += drawCurve(expr2, inMin2, inMax2, LHS=LHS2, style=style2, fillName='f2')
    
    # Make (invisible) top and bottom boundaries
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=top] {brackify(ymax)};'
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=bottom] {brackify(ymin)};'

    # Shade regions
    for count,jj in enumerate(endpts[:-1]):
        plot = True
        lower, upper = 'bottom', 'top'

        y1 = sympify(expr1).subs(x,jj+0.1)
        y2 = sympify(expr2).subs(x,jj+0.1)
        if {rel1,rel2}.issubset(aboves):
            lower = 'f1' if y1>y2 else 'f2'
        elif {rel1,rel2}.issubset(belows):
            upper = 'f1' if y1<y2 else 'f2'
        elif (rel1 in aboves) or (rel2 in aboves):
            lower = 'f1' if rel1 in aboves else 'f2'
            if (rel1 in belows) or (rel2 in belows):
                plot, upper = [(y2>y1), 'f2'] if rel2 in belows else [(y1>y2), 'f1']
        elif (rel1 in belows) or (rel2 in belows):
            upper = 'f1' if rel1 in belows else 'f2'
            if (rel1 in aboves) or (rel2 in aboves):
                plot, lower = [(y1>y2), 'f2'] if rel2 in aboves else [(y2>y1), 'f1']

        if plot:
            graph += shadeRegion(N(jj,2), N(endpts[count+1],2), lower, upper, color=color, shading=shading)

    graph += endGraph()

    return graph

def graphSysInequals2D_overlap(*inequals, xmin=-10, xmax=10, ymin=-10, ymax=10, colors=None, shadings=None):
    """
    Return LaTeX for system of inequalities graph.

    Parameters
    ----------
        inequals : array of inequality lists
            Enter inequalities as [rel, expr], RHS=expr and LHS=y unless included in rel.
    """
    
    aboves, belows = {'>','>=','=>','g','ge'}, {'<','<=','=<','l','le'}

    if shadings == None:
        shadings = ['vertical lines','horizontal lines','north east lines','north west lines','dots','fivepointed stars']
        shadings = ['pattern=' + jj for jj in shadings]
    colors = ['blue!70','red!70','green!70','yellow!70','cyan!70','magenta!70'] if colors==None else colors
    colors = ['pattern color=' + jj if 'pattern' in shadings[count] else jj for count,jj in enumerate(colors)]

    graph = startGraph(xmin, xmax, ymin, ymax)
    xmin, xmax, ymin, ymax = xmin-5, xmax+5, ymin-5, ymax+5

    # Make (invisible) top and bottom boundaries
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=top] {brackify(ymax)};'
    graph += fr'\addplot[draw=none, domain={xmin}:{xmax}, name path=bottom] {brackify(ymin)};'

    for count,jj in enumerate(inequals):
        rel, expr = jj[0].replace('y',''), jj[1]

        # Check for vertical boundary
        if 'x' in rel:
            inMin, inMax, LHS = ymin, ymax, 'x'
            left, right = [expr, xmax] if (rel.replace('x','') in aboves) else [xmin, expr]
        else:
            inMin, inMax, LHS = xmin, xmax, 'y'
            left, right = inMin, inMax

        # Draw boundary
        style = 'solid' if (('=' in rel) or ('e' in rel)) else 'dashed'
        graph += drawCurve(expr, inMin, inMax, LHS=LHS, style=style, fillName='f')

        # Make upper and/or lower boundaries
        if rel in aboves:
            upper, lower = 'top', 'f'
        elif rel in belows:
            upper, lower = 'f', 'bottom'
        else:
            upper, lower = 'top','bottom'

        # Shade region
        graph += shadeRegion(left, right, lower, upper, color=colors[count], shading=shadings[count])
    
    graph += endGraph()

    return graph

def graphPW(func, xmin=None, xmax=None, contDot=False):
    """
    Return LaTeX for piecewise graph.
    
    Parameters
    ----------
        func : PWFunc
        contDot : bool, default=False
            If True, draw dot at continuous junctions.
    """
    
    # Set graph limits
    if xmin == None:
        xmin = min(5*(func.domain.inf//5)-1, -1) if func.domain.inf!=-oo else -11
    if xmax == None:
        xmax = max(5*(func.domain.sup//5)+6, 1) if func.domain.sup!=oo else 11
    domain = func.domain.intersect(Interval(xmin,xmax))
    range = func.subSet(domain)
    ymin, ymax = min(5*(range.inf//5)-1, -1), max(5*(range.sup//5)+6, 1)
    
    graph = startGraph(xmin, xmax, ymin, ymax)
    
    # Graph pieces
    for count, pair in enumerate(func.pairs):
        interval = domain.intersect(pair[1])
        if interval != EmptySet:
            graph += drawCurve(pair[0], interval.start, interval.end, 'black')

            # Left endpoint for first interval
            if (count==0) and (interval.start==pair[1].start):                      
                pt = [interval.start, pair[0].subs(func.variable,interval.start)]
                fill = 'white' if interval.left_open else 'black'
                graph += drawPt(pt, fill=fill)

            # Left endpoint of current and right endpoint of previous
            if count != 0:
                pt = [interval.start, pair[0].subs(func.variable,interval.start)]
                prev = func.pairs[count-1]
                prevPt = [prev[1].end, prev[0].subs(func.variable,prev[1].end)]
                if pt == prevPt:
                    if pt[0] in domain:
                        graph += drawPt(pt, fill='black') if contDot==True else ''
                    else:
                        graph += drawPt(pt, fill='white')
                else:
                    fill = 'white' if interval.left_open else 'black'
                    graph += drawPt(pt, fill=fill)
                    fill = 'white' if prev[1].right_open else 'black'
                    graph += drawPt(prevPt, fill=fill)

            # Right endpoint for last interval
            if (count+1==len(func.pairs)) and (interval.end==pair[1].end):                      
                pt = [interval.end, pair[0].subs(func.variable,interval.end)]
                fill = 'white' if interval.right_open else 'black'
                graph += drawPt(pt, fill=fill)
    
    graph += endGraph()
    
    return graph

def graphPolygon(coords, labels=None, dots=True, color='black', thickness='thick'):
    mark = '*' if dots else 'none'
    string = fr'\addplot[{color},{thickness},mark={mark},'
    
    if labels == None:
        coords = [str(tuple(jj)) for jj in coords]
        coords = ' '.join(coords + [coords[0]])

        string += fr'] coordinates {brackify(coords)};'
    else:
        angles = []
        for count, jj in enumerate(coords):
            prev, next = Matrix(coords[count-1]), (Matrix(coords[count+1]) if count<len(coords)-1 else Matrix(coords[0]))
            vec = ((next-Matrix(jj)).normalized() + (prev-Matrix(jj)).normalized()).normalized()
            angle = -acos(vec[0]) if vec[1]<0 else acos(vec[0])
            angles.append(N(angle*180/pi,2))

        labels = [brackify(fr'\scriptsize${jj}$') for jj in labels] + [r'\,']
        coords, angles = coords+[coords[0]], angles+[0]
        coords = [fr'{N(jj[0],2)} {N(jj[1],2)} {labels[count]} {angles[count]}' for count,jj in enumerate(coords)]
        coords = r' \\ '.join(['x y label alignment'] + coords) + r' \\ '

        string += r'visualization depends on=\thisrow{alignment} \as \alignment,nodes near coords,'
        string += r'point meta=explicit symbolic,every node near coord/.style={anchor=\alignment}'
        string += fr'] table [meta index=2,row sep=\\] {brackify(coords)};'

    return string

def translateCoords(coords, shift):
    return [[jj[0]+shift[0],jj[1]+shift[1]] for jj in coords]

def rotateCoords(coords, angle, center=[0,0], clock='cw'):
    shifted = [[jj[0]-center[0], jj[1]-center[1]] for jj in coords]

    angle = -angle if clock in ['cw','clockwise'] else angle
    cosAngle, sinAngle = N(cos(pi*angle/180),6), N(sin(pi*angle/180),6)
    shifted = [[jj[0]*cosAngle-jj[1]*sinAngle, jj[0]*sinAngle+jj[1]*cosAngle] for jj in shifted]

    return [[jj[0]+center[0], jj[1]+center[1]] for jj in shifted]

def reflectCoords(coords, expr, LHS='y'):
    variables = list(sympify(expr).free_symbols)

    if (variables==[]) and (LHS in ['y',y]):        # Horizontal line
        return [[jj[0], 2*expr-jj[1]] for jj in coords]
    elif (LHS in ['x',x]):      # Vertical
        return [[2*expr-jj[0], jj[1]] for jj in coords]
    else:
        slope = expr.coeff(variables[0])
        shift = expr.coeff(variables[0],n=0)

        a, b, c = 1-slope**2, 2*slope, 1+slope**2
        a, b = a/c, b/c

        shifted = [[jj[0], jj[1]-shift] for jj in coords]
        shifted = [[a*jj[0]+b*jj[1], b*jj[0]-a*jj[1]] for jj in shifted]
        return [[jj[0], jj[1]+shift] for jj in shifted]

def getShape(shape, label1=None, bounds=[-10,10,-10,10]):
    coords = [randint(-5,5), randint(-5,5)]
    if shape == 2:                      # Segment
        coords = [coords, [coords[0]+getInt(-5,5), coords[1]+getInt(-5,5)]]
    elif shape == 3:                    # Triangle
        slope1, slope2 = Rational(getInt(-6,6),randint(2,4)), Rational(getInt(-6,6),randint(2,4))
        while slope2 == slope1:
            slope2 = Rational(getInt(-6,6),randint(2,4))
        coords = [coords, [coords[0]+slope1.q,coords[1]+slope1.p], [coords[0]+slope2.q,coords[1]+slope2.p]]
    elif shape == 4:                    # Rectangle or Parallelogram
        if randint(0,1):                            # Rectangle
            legs = [getInt(-5,5), getInt(-5,5)]
            coords = [[coords[0]+legs[0],coords[1]], coords, [coords[0],coords[1]+legs[1]]]
            coords += [[coords[0][0], coords[2][1]]]
        else:                                       # Parallelogram
            slopes = [getInt(-5,5), getInt(-5,5)]
            coords = [[coords[0]+1,coords[1]+slopes[0]], coords, [coords[0]+slopes[1],coords[1]+1]]
            coords += [[coords[2][0]+1, coords[2][1]+slopes[0]]]
    elif shape == 5:                    # "House" pentagon
        legs = [2*getInt(-3,3),getInt(-5,5)]
        height = randint(1,4) if legs[1]>0 else randint(-4,-1)
        coords = [[coords[0],coords[1]+legs[1]], coords, [coords[0]+legs[0],coords[1]]]
        coords += [[coords[2][0],coords[0][1]], [coords[1][0]+0.5*legs[0],coords[0][1]+height]]
        coords = rotateCoords(coords, choice([90,180,270]), [coords[4][0],coords[1][1]+0.5*legs[1]]) if randint(0,3) else coords
    elif shape == 6:                    # Hexagon (non-regular)
        legs = [2*getInt(-3,3),getInt(-5,5)]
        height = randint(1,2) if legs[1]>0 else randint(-2,-1)
        coords = [[coords[0],coords[1]+legs[1]], coords, [coords[0]+0.5*legs[0],coords[1]-height], [coords[0]+legs[0],coords[1]]]
        coords += [[coords[3][0],coords[0][1]], [coords[2][0],coords[0][1]+height]]
        coords = rotateCoords(coords, choice([90,180,270]), [coords[4][0],coords[1][1]+0.5*legs[1]]) if randint(0,3) else coords
    # elif shape == 7:                    # Arrow

    label1 = randint(ord('A'), ord('Z')-len(coords)+1) if label1==None else ord(label1)
    labels = [chr(label1+jj) for jj in range(len(coords))]

    return coords, labels

def getShapeToReflect(shape, func, label1=None, bounds=[-10,10,-10,10]):
    rise, run = func.slope.p, func.slope.q

    steps = [randint(-3,3), getInt(-3,3)]                                                       # Steps for first vertex
    coords = [steps[0]*run+steps[1]*rise, func.intercept+steps[0]*rise-steps[1]*run]

    steps = [steps, [getInt(-3,3,exclude=steps[0]),getInt(-3,3,exclude=[0,steps[1]])] ]         # Second vertex
    coords = [coords, [steps[1][0]*run+steps[1][1]*rise, func.intercept+steps[1][0]*rise-steps[1][1]*run] ]

    if shape > 2:                    # Third vertex
        steps.append([getInt(-3,3,exclude=[steps[0][0],steps[1][0]]),getInt(-3,3,exclude=[0,steps[0][1],steps[1][1]])])
        coords.append([steps[2][0]*run+steps[2][1]*rise, func.intercept+steps[2][0]*rise-steps[2][1]*run])
    if shape > 3:                    # Fourth vertex for parallelogram
        coords.append([coords[2][0]+coords[0][0]-coords[1][0], coords[2][1]+coords[0][1]-coords[1][1]])

    label1 = randint(ord('A'), ord('Z')-len(coords)+1) if label1==None else ord(label1)
    labels = [chr(label1+jj) for jj in range(len(coords))]

    return coords, labels

def drawRightTri(lengths, corner=None, labels=True):
    """
    Return LaTeX for right triangle.
    
    Parameters
    ----------
        lengths : array
            Hypotenuse must be last element.
        corner : string, default=None
            Location of right angle given as 'bl' or 'bottom left', 'tr' or 'top right', etc.
        labels : bool, or array of bools and strings, default=True
            Labels of sides
    """

    corner = choice(['bl','br','tl','tr']) if corner==None else corner

    if labels == True:
        labels = signify(latexify(lengths))
    else:
        for count, jj in enumerate(labels):
            if type(jj) == bool:
                labels[count] = signify(latexify(lengths[count])) if jj else '?'
            else:
                labels[count] = signify(jj)
    labels = [labels[0],labels[2],labels[1]]

    lengths = [round(jj,2) for jj in lengths]
    if corner in ['bl', 'bottom left']:
        coords = [(lengths[0],0), (0,lengths[1]), (0,0)]
        pos = ['below', 'above right', 'left']
    elif corner in ['br', 'bottom right']:
        coords = [(0,0), (lengths[0],lengths[1]), (lengths[0],0)]
        pos = ['below', 'above left', 'right']
    elif corner in ['tl', 'top left']:
        coords = [(lengths[0],lengths[1]), (0,0), (0,lengths[1])]
        pos = ['above', 'below right', 'left']
    else:
        coords = [(0,lengths[1]), (lengths[0],0), (lengths[0],lengths[1])]
        pos = ['above', 'below left', 'right']

    string = r'\begin{scaletikzpicturetowidth}{0.25\textwidth}\begin{tikzpicture}[scale=\tikzscale]'
    string += fr'\draw {coords[2]}'
    for jj in range(3):
        string += fr' -- {coords[jj]} node[midway,{pos[jj]}] {brackify(labels[jj])}'
    string += r'; \end{tikzpicture}\end{scaletikzpicturetowidth}'

    return string

def drawWheel(spokes, rim=True):
    string = r'\begin{scaletikzpicturetowidth}{0.25\textwidth}\begin{tikzpicture}[scale=\tikzscale]'
    string += r'\draw (0,0) circle (4cm);' if rim else ''
    
    angle = N(360/spokes,4)
    for jj in range(spokes):
        string += fr'\draw (0,0) -- ({jj*angle}:4);'

    string += r'\end{tikzpicture}\end{scaletikzpicturetowidth}'

    return string

# Below requires shapes.geometric tikz library
# \usetikzlibrary{shapes.geometric}
def drawRegPolygon(sides):
    string = r'\begin{scaletikzpicturetowidth}{0.25\textwidth}\begin{tikzpicture}[scale=\tikzscale]'
    string += fr'\node[regular polygon,draw,regular polygon sides={sides},minimum size=4cm] (p) at (0,0) '
    string += r'{};\end{tikzpicture}\end{scaletikzpicturetowidth}'

    return string