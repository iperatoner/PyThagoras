#!/usr/bin/env python3

# Berechnungen für sin und asin, kommen später zur Dreiecksklasse

from decimal import *
import math
PREC = 1500
PI = Decimal(str('''3.1415926535897932384626433832
                  795028841971693993751058209749
                  445923078164062862089986280348
                  253421170679821480865132823066
                  470938446095505822317253594081
                  284811174502841027019385211055
                  596446229489549303819644288109
                  756659334461284756482337867831
                  652712019091456485669234603486
                  104543266482133936072602491412
                  737245870066063155881748815209
                  209628292540917153643678925903
                  600113305305488204665213841469
                  519415116094330572703657595919
                  530921861173819326117931051185
                  480744623799627495673518857527
                  248912279381830119491298336733
                  624406566430860213949463952247
                  371907021798609437027705392171
                  762931767523846748184676694051
                  320005681271452635608277857713
                  427577896091736371787214684409
                  012249534301465495853710507922
                  796892589235420199561121290219
                  608640344181598136297747713099
                  605187072113499999983729780499
                  510597317328160963185950244594
                  553469083026425223082533446850
                  352619311881710100031378387528
                  865875332083814206171776691473
                  035982534904287554687311595628
                  638823537875937519577818577805
                  321712268066130019278766111959
                  092164201989380952572010654858
                  632788659361533818279682303019
                  520353018529689957736225994138
                  912497217752834791315155748572
                  424541506959508295331168617278
                  558890750983817546374649393192
                  550604009277016711390098488240
                  128583616035637076601047101819
                  429555961989467678374494482553
                  797747268471040475346462080466
                  842590694912933136770289891521
                  047521620569660240580381501935
                  112533824300355876402474964732
                  639141992726042699227967823547
                  816360093417216412199245863150
                  302861829745557067498385054945
                  8858692699569092721079750930296'''
                      ).replace("\n", "").replace(" ",""))


getcontext().prec = PREC

def pi():
    """Compute Pi to the current precision.

    >>> print pi()
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision


def sin(x):

    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def fakultaet(ya):

    fa = 1
    if ya == 0:
        return 1
    else:
        while ya != 0:
            fa = fa*ya
            ya = ya-1
    return fa


def asin(x):

    y = Decimal('0')
    n = Decimal('0')
    asin_numerator = fakultaet(Decimal('2')*n)
    asin_denominator = (Decimal('4')**n)*(fakultaet(n)**Decimal('2'))*(Decimal('2')*n+Decimal('1'))
    while n < 2:
        y += (asin_numerator/asin_denominator)*x**(Decimal('2')*n+Decimal('1'))
        n += 1
    return y

Winkel = int(input("Winkel: "))
Winkel2 = Winkel*PI/180
sinus = sin(Winkel2)
result_asin = math.asin(float(sinus))*180/float(PI)
print(result_asin)
