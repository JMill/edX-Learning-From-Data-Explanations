# dE/du (u e^v - 2v e^(-u))^2 = 2 (u e^v - 2v e^(-u))(e^v + 2v e^(-u))
#from decimal import Decimal
from math import sqrt, exp, fabs #natural exponent, e**x. and absolute value

def calcEwrtu(u,v):
    '''
    Given u and v, the hypothesis and the target function, 
    return the partial deriv w.r.t. u for gradient descent of the error.
    '''
    return 2 * ( u*exp(v) - 2*v*exp(-u) ) * ( exp(v) + 2*v*exp(-u) )

def calcEwrtv(u,v):
    '''
    Given u and v, the hypothesis and the target function, 
    return the partial deriv w.r.t. v for gradient descent of the error.
    '''
    return  2 * ( u * exp(v) - 2*v*exp(-u) ) * ( u*exp(v) - 2*exp(-u))

def calcE(u,v):
    return ( u*exp(v) - 2.*v*exp(-u) )**2


def q05():
    i = 0
    eta = 0.1 # u"\u03B7"
    u = 1.
    v = 1.
    #E = float(10^(-14))
    #E = 10^(-14)
    #E = Decimal(0.0000000000001)
    #E = 0.0000000000001
    E_threshold = 10e-14
    E = 99999.

    while True:
        if E < E_threshold:
            print E, '<', E_threshold, ' in', i, 'iterations'
            break
        else:
            dE_du = calcEwrtu(u,v)
            dE_dv = calcEwrtv(u,v)
            u = u - eta * dE_du
            v = v - eta * dE_dv
            E = calcE(u,v)
            #print 'E:', E, 'u:', u, 'v:', v, 'iter:', i
            i+=1
    return u, v, E, i

print q05()

def euclidDist(x1, y1, x2, y2):
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )

def q06():
    choices = { 
        "a": [1.,1.],
        "b": [0.713, 0.045],
        "c": [0.016, 0.112],
        "d": [-0.083, 0.029],
        "e": [0.045, 0.024]
    }

    u1, v1, _, _ = q05()
    closestChoice = ''
    closestDistance = 999

    for choice in choices:
        u2,v2 = choices[choice]
        distanceBetweenValues = euclidDist(u1, v1, u2, v2)
        if distanceBetweenValues < closestDistance:
            closestDistance = distanceBetweenValues
            closestChoice = choice
    return closestChoice, closestDistance

print q06()


