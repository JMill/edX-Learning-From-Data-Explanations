import matplotlib.pylab as pylab
import math

d_vc = 50.
delta = 0.05
epsilon = 0.05
N = 10000.
#def choice_a(N):
#    return (8/N*math.log(4*(2*N)**d_vc/delta))**0.5
#print choice_a(N)
'''
b = lambda N: (8/N*math.log(4*(2*N)**d_vc/delta))**0.5
print b(N)
'''
bounds = {
    'a': lambda N: math.sqrt(8/N*math.log(4*(2*N)**d_vc/delta)) ,
    'b': lambda N: math.sqrt(2/N * math.log(2*N*N**d_vc)) + math.sqrt( 2/N * math.log( 1/delta )) + 1/N , 
    'c': lambda N: math.sqrt( 1/N*(2*epsilon + math.log(6*(2*N)**d_vc/delta)) )  ,
    'd': lambda N: math.sqrt( 1/(2*N)* (4*epsilon*(1+epsilon) + math.log( 4*((N**2)**(d_vc))/delta )) )
}

print bounds['a'](N)
print bounds['b'](N)
print bounds['c'](N)
#print bounds['d'](N) # "Result too large" error

N = 5.
bounds = {
    'a': lambda N: math.sqrt(8/N*math.log(4*2**(2*N)/delta)) ,
    'b': lambda N: math.sqrt(2/N * math.log(2*N*2**N)) + math.sqrt( 2/N * math.log( 1/delta )) + 1/N , 
    'c': lambda N: math.sqrt( 1/N*(2*epsilon + math.log(6*(2**(2*N))/delta)) )  ,
    'd': lambda N: math.sqrt( 1/(2*N)* (4*epsilon*(1+epsilon) + math.log( 4*((2**N**2)/delta )) ))
}

print bounds['a'](N)
print bounds['b'](N)
print bounds['c'](N)
print bounds['d'](N)