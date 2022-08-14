from Imports import *
from Generators import tableGenerator
from Classes import LinFunc
from Graphing import drawScatter, getGraphBounds
#startNumLine, endNumLine

def genData1D(xmin=-5, xmax=5, p=0.5, size=50):
    # TODO: binom vs nbinom for longer tails
    return stats.nbinom.rvs(n=xmax-xmin, p=p, size=size) + xmin

def getFreqs(data):
    xmin, xmax = min(data), max(data)
    freqs = []
    for jj in range(xmin,xmax+1):
        if jj in data:
            freqs += [[jj, sum([kk==jj for kk in data])]]
    
    return np.array(freqs), 5*(xmin//5), 5*(xmax//5+1)

def dotPlot(data):
    data = np.array(data)
    if len(data.shape) == 1:
        data, xmin, xmax = getFreqs(data)
    else:
        xmin, xmax = 5*(min(data[:,0])//5), 5*(max(data[:,0])//5+1)
    
    coordinates = []
    for jj in data:
        coordinates += [[jj[0],0.4*kk] for kk in range(1,jj[1]+1)]

    return startNumLine(xmin, xmax) + drawScatter(coordinates,draw='blue') + endNumLine()

def boxPlot(data):
    quants = np.quantile(data, [0,0.25,0.5,0.75,1])

    string = startNumLine(5*(quants[0]//5), 5*(quants[4]//5+1))
    string += r'\addplot[boxplot prepared={'
    string += fr'median={quants[2]},upper quartile={quants[3]},lower quartile={quants[1]},upper whisker={quants[4]},lower whisker={quants[0]}'
    string += r'},] coordinates {};' + endNumLine()

    return string

def genData2D(func, std, xmin=0, xmax=10, size=50):
    data = np.array([[jj,func.subs(jj)] for jj in np.linspace(xmin,xmax,size)])
    data[:,1] += stats.norm.rvs(scale=std,size=size)

    return np.around(data.astype(float),decimals=2)

def bestFitLine(data):
    slope, intercept, corrCoeff, _, _ = stats.linregress(data)

    return LinFunc(slope, intercept), corrCoeff

def drawResids(data, func, color='red', thickness='thick'):
    string = ''
    for pair in data:
        coords = fr'{tuple(pair)} ({pair[0]},{func.subs(pair[0])})'
        string += fr'\addplot[{color},{thickness}] coordinates {brackify(coords)};'

    return string

def residPlot(data, func):
    resids = [[pair[0],pair[1]-func.subs(pair[0])] for pair in data]
    bounds = getGraphBounds(resids)

    string = startGraph(*bounds) + drawResids(resids, LinFunc(0,0))
    string += drawScatter(resids) + endGraph()
    
    return string

def genData2Way(probs, total, indep=False):
    probs = [[jj] if type(jj)!=list else jj for jj in probs]
    splits = [[round(kk*total) for kk in jj] for jj in probs]

    if not indep:
        jointprobs = splits[1].copy()
        for ll in range(len(splits[1])):
            partition = [random.uniform(0.1,0.9) for jj in probs[0]]
            partition.sort()
            jointprobs[ll] = [jj - partition[count-1] if count>0 else jj for count,jj in enumerate(partition)]
        joints = [[round(jj*kk) for kk in (jointprobs[count])] for count,jj in enumerate(splits[1])]
    else:
        joints = [[round(jj*kk) for kk in probs[0]] for jj in splits[1]]
    
    splits = [jj + [total-sum(jj)] for jj in splits]
    data = [jj + [splits[1][count]-sum(jj),splits[1][count]] for count,jj in enumerate(joints)]
    data += [[splits[0][count]-sum(jj) for count,jj in enumerate(np.array(data).transpose()[:-1])] + [splits[1][-1]]]
    data += [splits[0] + [total]]

    return data

def twoWayTable(data, labels, totals=True):
    if totals:
        rows = data.copy()
    else:
        rows = [jj + [sum(jj)] for jj in data]
        rows += [[sum(jj) for jj in np.array(rows).transpose()]]

    labels = [[r'\bf ' + kk for kk in jj] + [r'\bf Total'] for jj in labels]
    header = [''] + labels[0]
    rows = [[labels[1][count]] + jj for count,jj in enumerate(rows)]

    return tableGenerator(header, rows)