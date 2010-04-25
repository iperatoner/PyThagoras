# Berechnungen für sin und asin, kommen später zur Dreiecksklasse

from decimal import *
getcontext().prec = 1500

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

    y = 0
    n = 0
    while n < 1000:
        y += ((fakultaet(2*n))/((4**n)*(fakultaet(n))**2*(2*n+1)))*x**(2*n+1) # alle Werte zu decimals machen
        n += 1
    return y

"""Winkel = int(input("Winkel: "))
Winkel2 = Winkel*pi()/180
sinus = sin(Winkel2)
result_asin = asin(sinus)*180/pi()
print(result_asin)"""
