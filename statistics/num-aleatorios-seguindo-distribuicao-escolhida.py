#! /usr/bin/python

import random
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print
 
sigma = 0.15
listaFull = []
listaHalf = []

for i in range(0,10000):

  chi1 = random.uniform(0,1)
  chi2 = random.uniform(0,1)
  eta1 = math.sqrt(-2.0*sigma ** 2 * math.log(chi1)) * math.cos(2*math.pi*chi2)
  eta2 = math.sqrt(-2.0*sigma ** 2 * math.log(chi1)) * math.sin(2*math.pi*chi2)

  listaFull.append(eta1)
  listaFull.append(eta2)

  #print eta1, eta2
  #print
  #print lista

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
n, bins, patches = plt.hist(listaFull, 50, normed=1, facecolor='green', alpha=0.75)

plt.xlabel('Numbers')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ random\ numbers\ \eta_{1}\ and\ \eta_{2} }\ $')
plt.axis([-1, 1, 0, 3.0])
plt.grid(True)

#plt.show()

fig.savefig('eta1-and-eta2-gaussian-dist.png', dpi=fig.dpi)

chi1 = 0
chi2 = 0
eta1 = 0
eta2 = 0

for i in range(0,10000):

  chi1 = random.uniform(0,1)
  chi2 = random.uniform(0,1)
  eta1 = math.sqrt(-2.0*sigma ** 2 * math.log(chi1)) * math.cos(2*math.pi*chi2)
  #eta2 = math.sqrt(-2.0*sigma ** 2 * math.log(chi1)) * math.sin(2*math.pi*chi2)

  listaHalf.append(eta1)

#  print eta1

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
n, bins, patches = plt.hist(listaHalf, 50, normed=1, facecolor='green', alpha=0.75)

plt.xlabel('Numbers')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ random\ numbers\ only\ \eta_{1}}\ $')
plt.axis([-1, 1, 0, 3.0])
plt.grid(True)

#plt.show()

fig.savefig('only-eta1-gaussian-dist.png', dpi=fig.dpi)

# following exponential distribution

chi1 = 0
chi2 = 0
eta1 = 0
eta2 = 0

lista = []

for i in range(0,10000):

  chi = random.uniform(0,1)
  eta = math.exp(-chi)

  lista.append(eta)

#  print eta
#  print chi, eta

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
n, bins, patches = plt.hist(lista, 50, normed=1, facecolor='green', alpha=0.75)

plt.xlabel('Number')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ random\ numbers\ exp(-x)\ dist.}\ $')
plt.axis([0.2, 1.2, 0, 3.0])
plt.grid(True)

#plt.show()

fig.savefig('exponential-dist.png', dpi=fig.dpi)

print





