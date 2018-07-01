#! /usr/bin/python

# Example page 51 of Chorin
# We want to calculate the mean value using Monte Carlo with and without 'importance sampling'

import random
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print

def func1(x,N):
  valor1 = 0.0
  valor1 = (1.0/N) * math.cos(x/5.0) * math.exp(-5*x)
  return valor1 

def func2(J,y,M,j):
  valor2 = 0.0
  valor2 = (J/M) * math.cos(y/5.0)
  return valor2 

n = 1000

Itheo = 0.1983725855   # result of Int(cos(x/5)*exp(-5*x), x=0..1)
Iexp1 = 0.0            # approximation to Itheo by method 1
Iexp2 = 0.0            # approximation to Itheo by method 2

lista_numChi1 = []
lista_numChi2 = []
lista_numEta = []

testeFunc1 = []
testeFunc2 = []

for i in range(0,n):
  chi = random.uniform(0,1)

  lista_numChi1.append(chi)  # just in case I want some histogram; otherwise, it is not necessary

  Iexp1 = Iexp1 + func1(chi,n)

  testeFunc1.append(func1(chi,n))

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
m, bins, patches = plt.hist(testeFunc1, 50, normed=0, facecolor='green', alpha=0.75)

plt.xlabel('Numbers')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ random\ numbers\ cos(x)*exp(-x) }\ $')
plt.axis([-0.000, 0.0012, 0, 300.0])
plt.grid(True)

#plt.show()

fig.savefig('hist-cos-exp.png', dpi=fig.dpi)

I1 = 0.1986524106   # result of Int(exp(-5*x), x=0..1)
chi = 0.0

for i in range(0,n):
  chi = random.uniform(0,1)

  lista_numChi2.append(chi)  # just in case I want some histogram; otherwise, it is not necessary

  eta = - 1.0/5.0 * math.log(1.0 - 5.0 * I1 * chi)

  lista_numEta.append(eta)   # just in case I want some histogram; otherwise, it is not necessary

  Iexp2 = Iexp2 + func2(I1,eta,n,i)

  #print 'no for', 'eta =', eta, 'func2 =', func2(I1,eta,n,i), 'termo =', (I1/n) * math.cos(eta/5.0), 'i =', i, 'soma =', Iexp2
  
  testeFunc2.append(func2(I1,eta,n,i))

print max(testeFunc2), min(testeFunc2)

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
m, bins, patches = plt.hist(testeFunc2, 50, normed=0, facecolor='green', alpha=0.75)

plt.xlabel('Numbers')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ random\ numbers\ cos(x) }\ $')
plt.axis([0.000194, 0.00020, 0, 500.0])
plt.grid(True)

#plt.show()

fig.savefig('hist-cos.png', dpi=fig.dpi)

print 'n = ', n
print 'I_theor = ', Itheo, 'I_meth_1 =', Iexp1, 'I_meth_2 = ', Iexp2


print









