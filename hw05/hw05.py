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


def q07():
    '''
    'coordinate descent':
    1. move only along u coordinate to reduce error.
    2. reevalute and move only along the v coordinate to reduce the error.

    returns E(u,v) after 15 epochs (iterations).
    '''
    i = 0
    eta = 0.1
    u = 1.0
    v = 1.0

    while i < 15:
        u = u - eta * calcEwrtu(u, v)
        v = v - eta * calcEwrtv(u, v)
        i += 1
    return calcE(u, v)


##################
# Exercises 8, 9, 10
##################


# from hw02

import random
import numpy
import numpy.linalg

#  ###########################

def generatePoints(numberOfPoints):
    '''
    Note: Generates Points as well as an target function.

    Returns two points that determine the target function (a line),
    as well as a list of random points and their binary classification 
    (as -1 or +1) based on being below or above the target line.

    format:
    (target x1, target y1, target x2, target y2, [list of classified points as [ 1 (threshold), x coord, y coord, 1 or -1 classification])
    '''
    #generate two points for target function
    x1 = random.uniform( -1, 1 )
    y1 = random.uniform( -1, 1 )
    x2 = random.uniform( -1, 1 )
    y2 = random.uniform( -1, 1 )
    points = []

    #generate random points and classify them based on target function
    for point in range(numberOfPoints):
        x = random.uniform( -1, 1 )
        y = random.uniform( -1, 1 )
        points.append([1, x, y, targetFunctionResult(x1, y1, x2, y2, x, y)]) # ( threshold, xcoord, ycoord, -1/+1 binar output)
    return x1, y1, x2, y2, points


def targetFunctionResult(x1, y1, x2, y2, testx, testy):
    # based on: http://stackoverflow.com/questions/3461453/determine-which-side-of-a-line-a-point-lies
    u = (x2-x1)*(testy-y1) - (y2-y1)*(testx-x1)
    if u >= 0:
        return 1
    else:
        return -1

def linearRegression(points):
    '''
    The data is located in the input list's position 3. Format:
        [ threshold (1), xcoord, ycoord, classification (-1 or +1) ]

    Based on "linear regression algortithm" on Lecture 03 slide 17.

    Returns the weights as a 3-item list.
    '''
    X = []
    y = []
    y_location = len(points[0]) - 1 # locate the binary class value, which is in last position
    for point in points:
        X.append(point[:y_location]) # Add [1, randx, randy ], as numpy array
        y.append(point[y_location]) # add the binary class value (is a -1 or +1)

    #X = numpy.array(X) # conversion not required?
    #y = numpy.array(y) # conversion not required?

    X_psuedo_inverse = numpy.linalg.pinv(X)
    w = numpy.dot( X_psuedo_inverse, y ) # calculate the weights directly.
    return w


def perceptron( points, weights = numpy.zeros(3), maxIterations = 1000 ):
    '''
    '''
    isLearned = False
    y_location = len(points[0]) - 1 # Assume that classification (y) is last item
    i = 0

    while not isLearned or (i < maxIterations):
        misclassifiedPoints = []
        for point in points:
            x = point[:y_location] # x is a vector. [ 1, xcoord, ycoord ]
            y = point[y_location] # y is a binary classification. -1 or 1
            # Look for misclassified points based on the current weights.
            if numpy.sign(numpy.dot(weights, x)) != y:
                misclassifiedPoints.append(point)
        if len(misclassifiedPoints) == 0:
            isLearned = True
            break
        else:
            # pick a misclassified point and update the weight vector
            misclassifiedPoint = random.choice(misclassifiedPoints)
            misclass_x = misclassifiedPoint[:y_location]
            misclass_y = misclassifiedPoint[y_location]
            weights = weights + ( numpy.dot(misclass_y, misclass_x) )
        i+=1
    if i >= maxIterations:
        print "Quit after", i, "iterations."
    #print "Learned?", isLearned, "after", i, "iterations."
    return weights, isLearned, i

def runExperiment(numberOfPoints, numberOfTrials):
    numberOfIterations = 0.
    for trial in range(numberOfTrials):
        # Find weights with Linear Regression
        _, _, _, _, points = generatePoints(numberOfPoints) # x1,y1,x2,y2,points
        weights = linearRegression(points)
        #print weights

        # Run PLA initialized with LR's weights
        weights, isLearned, iterations = perceptron(points, weights)
        if isLearned:
            numberOfIterations += iterations
    return numberOfIterations / numberOfTrials

# end hw02 regression/PLA code

def q08():
    N = 100
    trials = 100
    return runExperiment(N, trials)



#######################################
# generate solutions for each exercise
#######################################
#print q05()
#print q06()
#print q07()
print q08()
