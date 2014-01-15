# dE/du (u e^v - 2v e^(-u))^2 = 2 (u e^v - 2v e^(-u))(e^v + 2v e^(-u))
#from decimal import Decimal
from math import exp #natural exponent, e**x

def calcE(u,v):
    return 2 * ( u*exp(v) - 2*v*exp(-u) ) * ( exp(v) + 2*v*exp(-u) )

i = 0
eta = 0.1 # u"\u03B7"
#E = float(10^(-14))
#E = 10^(-14)
#E = Decimal(0.0000000000001)
#E = 0.0000000000001
E_threshold = 10e-14

print calcE(1,1)
'''
while True:
    if E < E_threshold:
        print E, '<', E_threshold, ' in', i, 'iterations'
        break
    else:
'''