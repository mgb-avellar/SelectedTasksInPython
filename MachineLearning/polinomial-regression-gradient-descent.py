#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Ellipse
import matplotlib as mpl
import os; os.getcwd(); os.walk('.')
from matplotlib import rcParams
rcParams['ps.fonttype'] = 42 

#### ======================= Defining functions =======================

def computeCost(Xnew, y2, theta):

#COMPUTECOST Compute cost for linear regression
#   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
#   parameter for linear regression to fit the data points in X and y

# Initialize some useful values
   m = len(y2) # number of training examples
   #print 'm', m

   J = 0.0
   #print 'Xnew inside J', Xnew.shape, theta.shape
   predictions = np.dot(Xnew,theta)						# predictions for the hypothesis for all m examples
   #print predictions, predictions.shape
   
   predictionsMinusPrices = np.subtract(predictions,y2)	
   #print sqrErrors, sqrErrors.shape

   sqrErrors = np.multiply(predictionsMinusPrices,predictionsMinusPrices)	# squared errors
   #print sqrErrors, sqrErrors.shape

   J = 1.0/(2.0*m) * np.sum(sqrErrors)						# sum over the squared errors

   return J


def gradientDescent(X, y, theta, alpha, num_iters):

#GRADIENTDESCENT Performs gradient descent to learn theta
#   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
#   taking num_iters gradient steps with learning rate alpha

# Initialize some useful values
   m = len(y); # number of training examples
   J_history = np.zeros([num_iters, 1])

   #print 
   #print 'Optimum theta:'
   #print 

   for iter in range(0,num_iters):

    # ====================== YOUR CODE HERE ======================
    # Instructions: Perform a single gradient step on the parameter vector
    #               theta. 
    #
    # Hint: While debugging, it can be useful to print out the values
    #       of the cost function (computeCost) and gradient here.
    #
	hypothesis = np.dot(X,theta)
	#print 'inside grad', X.shape, theta.shape
	#print 'inside grad hyp', hypothesis
	errorVec = np.subtract(hypothesis,y)
	

	#print X.shape, len(X[1,:])
       
	#feat1 = np.array([X[:,0]]).transpose()
	#print 'feat1', feat1, feat1.shape
	#print
	#errFeat1 = np.multiply(errorVec,feat1)
	#print
	#print 'errFeat1', errFeat1, errFeat1.shape

	#feat2 = np.array([X[:,1]]).transpose()
	#print 'feat2', feat2, feat2.shape
	#print
	#errFeat2 = np.multiply(errorVec,feat2)
	#print
	#print 'errFeat2', errFeat2, errFeat2.shape

	for k in range(0,len(X[1,:])):
           theta[k,0] = theta[k,0] - alpha * 1.0 / (m) * np.sum(( np.multiply(errorVec,np.array([X[:,k]]).transpose()) ))
        
       
	#theta[0,0] = theta[0,0] - alpha * 1.0 / (m) * np.sum(( np.multiply(errorVec,np.array([X[:,0]]).transpose()) ))
	#theta[1,0] = theta[1,0] - alpha * 1.0 / (m) * np.sum(( np.multiply(errorVec,np.array([X[:,1]]).transpose()) ))


        # Save the cost J in every iteration    
        J_history[iter] = computeCost(X, y, theta)

   #print theta

   return theta, J_history

def FeatNormalization(X):
#FEATURENORMALIZE Normalizes the features in X 
#   FEATURENORMALIZE(X) returns a normalized version of X where
#   the mean value of each feature is 0 and the standard deviation
#   is 1. This is often a good preprocessing step to do when
#   working with learning algorithms.

# You need to set these values correctly
   Xnorm = X
   mu = np.zeros([1, len(X[1,:])])
   sigma = np.zeros([1, len(X[1,:])])

   #print 'inside norm', Xnorm.shape, mu, sigma

# ====================== YOUR CODE HERE ======================
# Instructions: First, for each feature dimension, compute the mean
#               of the feature and subtract it from the dataset,
#               storing the mean value in mu. Next, compute the 
#               standard deviation of each feature and divide
#               each feature by it's standard deviation, storing
#               the standard deviation in sigma. 
#
#               Note that X is a matrix where each column is a 
#               feature and each row is an example. You need 
#               to perform the normalization separately for 
#               each feature. 
#
# Hint: You might find the 'mean' and 'std' functions useful.
#

   partial = np.zeros([1, len(X[1,:])])
   #print partial[0,1]

   for i in range(0,len(X[:,1])):

      for j in range(0,len(X[1,:])):

         partial[0,j] = partial[0,j] + X[i,j];


   for j in range(1,len(X[1,:])):

      mu[0,j] = partial[0,j] / len(X[:,1])
      sigma[0,j] = np.std(X[:,j])
      #sigma(j) = max(X(:,j))-min(X(:,j))
      Xnorm[:,j] = (Xnorm[:,j] - mu[0,j]) / sigma[0,j]

#   print 'partial', partial

   print 'mu',mu

   print 'sigma', sigma

#   print 'Xnorm', Xnorm

       


   return Xnorm

#### ======================= Defining functions =======================





print 

#### ======================= Part 1: Plotting data =======================

# data file
infile = 'ex1data1.txt'
#

# loading data
data=np.loadtxt(infile)

temp = np.loadtxt('teste4')

#print 'temp', temp.shape
numCols = len(temp[1,:])
#print 'numcols', numCols

listaCols = range(0,numCols-1)
#print listaCols
input_data = np.loadtxt('teste4', dtype='f', usecols=listaCols)

#print input_data
#print 'input shape',input_data.shape

X = input_data[:,0]

y = temp[:,numCols-1]

del temp

m = len(y)

#print m

# plotting data
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('auto')

ax.errorbar(X, y, fmt="o", color='red', markersize='7', label='Observational')

#plt.axis([4, 24, -5, 25])
plt.axis([450, 2200, 80, 320])
plt.xlabel(r'Profit in $10,000s')
plt.ylabel(r'Population of City in 10,000s')
plt.title(r'Dataset 1, exercise 1: food truck profit')

# Now add the legend with some customizations.
legend = ax.legend(loc='upper left', shadow=True, numpoints = 1)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.9999')

#plt.show()

fig.savefig('food-truck-profit-1D-teste.png')

#### ======================= Part 1: Plotting data =======================

#### ======================= Part 2: Cost and Gradient descent ===========

#theta = np.zeros([2, 1])

#print theta

# Adding ones to X matrix for the intercept
# X2: transforming X in a (1,97) matrix and taking its transpose ...
#  ... in order to have a (97,1) matrix to which add the ones.
X0 = np.ones((m,1))
X2 = np.array([X]).transpose()
X3 = input_data

#print 'X3', X3.shape

# For my particular exemple
#X0 = np.dot(X0,-1)


Xnew = np.hstack((X0,X3))

y2 = np.array([y]).transpose()

print Xnew

theta = np.zeros([len(Xnew[1,:]), 1])

print Xnew.shape
print theta.shape
print y2.shape

##
# precisa entrar a normalizacao
##

Xnorm = FeatNormalization(Xnew)
# print 'Xnorm', Xnorm

#J = computeCost(Xnew, y2, theta)
J = computeCost(Xnorm, y2, theta)

print 'The cost function J is', J

#print 'Additional test on J function:', computeCost(Xnew, y2, [[-1.0],[2.0]])

iterations = 1500
alpha = 0.01

bestTheta, minJ = gradientDescent(Xnorm, y2, theta, alpha, iterations)

print
print 'Optimum theta:'
print bestTheta
print
print 'Minimum J achieved:'
print minJ[iterations-1]

#### ======================= Part 3: Plotting results =======================

# data file
infile = 'ex1data1.txt'
#

# loading data
data=np.loadtxt(infile)

temp = np.loadtxt('teste4')

#print 'temp', temp.shape
numCols = len(temp[1,:])
#print 'numcols', numCols

listaCols = range(0,numCols-1)
#print listaCols
input_data = np.loadtxt('teste4', dtype='f', usecols=listaCols)

#print input_data
#print 'input shape',input_data.shape

X = input_data[:,0]

y = temp[:,numCols-1]

del temp

m = len(y)

#print m

# plotting data
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('auto')

ax.errorbar(X, y, fmt="o", color='red', markersize='7', label='Observed prices')

#plt.axis([4, 24, -5, 25])
plt.axis([450, 2200, 80, 320])
plt.xlabel(r'Profit in $10,000s')
plt.ylabel(r'Population of City in 10,000s')
plt.title(r'Dataset 1, exercise 1: food truck profit')

# plotting the best fit
line1, = ax.plot(X, np.dot(Xnorm,bestTheta), '-', linewidth=1, label='Best linear fit to data')

print 'X e np.dot shapes', X.shape, np.dot(Xnorm,bestTheta).shape
print 'np.dot', np.dot(Xnorm,bestTheta)
print
print 'Xnorm', Xnorm

# Now add the legend with some customizations.
legend = ax.legend(loc='upper left', shadow=True, numpoints = 1)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.9999')

#plt.show()

fig.savefig('food-truck-profit-1D-plus-best-fit-teste.png')


#xxxx

# plotting J convergence

iterationsArray = np.arange(0,iterations,1)
Jconvergence = minJ

#print 'iterationsArray and J shapes', iterationsArray.shape, Jconvergence.shape

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('auto')

#plt.axis([0.1, 1500, 4, 7])
plt.axis([0.1, 1500, 600, 6000])
plt.xlabel(r'Number of iterations')
plt.ylabel(r'J value')
plt.title(r'Dataset 1, exercise 1: food truck profit')

# plotting the best fit
line2, = ax.plot(iterationsArray, Jconvergence, '--', linewidth=2, label='J convergence')
#ax.set_xscale('log')


# Now add the legend with some customizations.
legend = ax.legend(loc='upper right', shadow=True, numpoints = 1)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.9999')

#plt.show()

fig.savefig('food-truck-profit-1D-J-convergence-teste.png')

#### ======================= Part 3: Plotting results =======================






print
