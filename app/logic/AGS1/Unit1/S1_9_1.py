import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# 1.9.1 Which Grows Faster?
# instruction : find the first five terms. Then compare the growth of the arithmetic sequence and the geometric sequence. Which grows faster? When?

def Which_Grows_Faster(case=1, expr='latex'):
    if case == 1: # Same start and common w/ growth
        start, common = randint(1,5), randint(2,5)
        arith, geo = ArithSeq(common,[1,start]), GeoSeq(common,[1,start], label='g')

        answer = r'{\bf b. }' + fr'${geo.label}(100)>{arith.label}(100)$: geometric growth always outgrows arithmetic growth eventually.'
    elif case == 2: # Arith: small start w/ growth, Geo: big start w/ decay
        arith = ArithSeq(randint(5,15), randint(1,4))
        geo = GeoSeq(Rational(1,randint(2,5)), [5,randint(1,5)], label='g')

        answer = r'{\bf b. }' + fr'${arith.label}(100)>{geo.label}(100)$: arithmetic growth will eventually exceed geometric decay.'
    elif case == 3: # Arith: big start w/ growth, Geo: small start w/ growth
        arith = ArithSeq(randint(5,15), [1,randint(200,300)])
        geo = GeoSeq(randint(2,5), [1,randint(1,5)], label='g')

        answer = r'{\bf b. }' + fr'${geo.label}(100)>{arith.label}(100)$: geometric growth always outgrows arithmetic growth eventually.'
    elif case == 4: # Arith: big start w/ decay, Geo: small start w/ growth
        arith = ArithSeq(randint(-15,-5), [1,randint(100,200)])
        geo = GeoSeq(randint(2,5), randint(1,5), label='g')

        answer = r'{\bf b. }' + fr'${geo.label}(100)>{arith.label}(100)$: geometric growth will eventually exceed arithmetic decay.'
    elif case == 5: # Same (big) start and (similar) common w/ decay
        geo = GeoSeq(Rational(1,randint(2,5)), [5,randint(1,5)], label='g')
        arith = ArithSeq(-1/geo.common, [1,geo.start])

        answer = r'{\bf b. }' + fr'${geo.label}(100)>{arith.label}(100)$: arithmetic decay eventually becomes negative while geometric decay remains positive.'


    info = randint(1,3)
    if info == 1:
        arithInfo = fr'{arith.label}(1) = {latexify(arith.start, arith.precision)}, '
        arithInfo += r'\text{ common difference } d = ' + latexify(arith.common, arith.precision)
        geoInfo = fr'{geo.label}(1) = {latexify(geo.start, geo.precision)}, '
        geoInfo += r'\text{ common ratio } r = ' + latexify(geo.common, geo.precision)
    elif info == 2:
        arithInfo, geoInfo = arith.getRecursive(), geo.getRecursive()
    elif info == 3:
        arithInfo, geoInfo = arith.getExplicit(), geo.getExplicit()

    header = ['$n$', f'${arith.label}(n)$', f'${geo.label}(n)$']
    images = [[signify(latexify(arith.subs(jj), arith.precision)), signify(latexify(geo.subs(jj), geo.precision))] for jj in range(1,6)]
    rows = [[f'${jj+1}$', fr'\phantom{brackify(images[jj][0])}', fr'\phantom{brackify(images[jj][1])}'] for jj in range(5)]

    problem = 'Arithmetic sequence: ' + signify(arithInfo) + r'\newline '
    problem += 'Geometric sequence: ' + signify(geoInfo) + r'\newline '
    problem += r'{\bf a. }' + tableGenerator(header, rows)
    problem += r'{\bf b. }' + f'Which value will be greater, ${arith.label}(100)$ or ${geo.label}(100)$? Why?'

    rows = [[f'${jj+1}$', images[jj][0], images[jj][1]] for jj in range(5)]
    answer = r'{\bf a. }' + tableGenerator(header, rows) + answer

    return problem, answer