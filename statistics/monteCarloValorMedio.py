#! /usr/bin/python

# Example page 51 of Chorin
# We want to calculate the mean value using Monte Carlo with and without 'importance sampling'

import random
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print

n = 10000

Itheo = 0.1983725855   # result of Int(cos(x/5)*exp(-5*x), x=0..1)
Iexp1 = 0.0            # approximation to Itheo by method 1
Iexp2 = 0.0            # approximation to Itheo by method 2

lista_numChi1 = []
lista_numChi2 = []
lista_numEta = []

for i in range(0,n):
  chi = random.uniform(0,1)

  lista_numChi1.append(chi)  # just in case I want some histogram; otherwise, it is not necessary

  Iexp1 = Iexp1 + (1.0/n) * math.cos(chi/5.0) * math.exp(-5*chi)

I1 = 0.1986524106   # result of Int(exp(-5*x), x=0..1)
chi = 0.0

for i in range(0,n):
  chi = random.uniform(0,1)

  lista_numChi2.append(chi)  # just in case I want some histogram; otherwise, it is not necessary

  eta = - 1.0/5.0 * math.log(1.0 - 5.0 * I1 * chi)

  lista_numEta.append(eta)   # just in case I want some histogram; otherwise, it is not necessary

  Iexp2 = Iexp2 + (I1/n) * math.cos(eta/5.0)

  #print Iexp2, (I1/n) * math.cos(eta/5.0), I1, n, i

print 'n = ', n
print 'I_theor = ', Itheo, 'I_meth_1 =', Iexp1, 'I_meth_2 = ', Iexp2


print









