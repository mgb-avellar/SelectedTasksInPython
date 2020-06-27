#! /usr/bin/python

# Playing with histograms and dices of # sides chosen by the user
# We want to calculate some statistics about the probabilities of a given sum of
#   the numbers of the face of each dice

import random
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print

num_sides_each_dice = []
num_face_dice = []
Sum = 0
Sum_vector = []
HistMax = 0
HistMin = 0

N = int(raw_input('Enter with the number of dice (greater than 1): '))

while N <= 1:
  N = int(raw_input('Enter with the number of dice (greater than 1): '))

else:
  print 'The number of dice is: ', N

print 'Now you are going to say how many sides have each dice.'

for i in range(1,N+1):  
  print 'Dice # ', i

  sides = int(raw_input('Number of sides  (greater than 2): '))
  
  while sides < 2:
    sides = int(raw_input('Number of sides  (greater than 2): '))
  else:
    num_sides_each_dice.append(sides)
    

print num_sides_each_dice

HistMin = N

for i in range(len(num_sides_each_dice)):
  HistMax = HistMax + num_sides_each_dice[i]

#print Hist

# Generating random numbers for each dice face in M experiments

M = int(raw_input('Enter how many experiments you want (greater than or equal to 1): '))

while M < 1:
  M = int(raw_input('Enter how many experiments you want (greater than or equal to 1): '))

else:
  print 'You are throwing the dices ', M, 'times.'

for j in range(1,M+1):

  for i in range(1,N+1):
    numero = int(random.uniform(1,num_sides_each_dice[i-1]+1))
    #numero = random.randint(1,num_sides_each_dice[i-1])

    if numero > num_sides_each_dice[i-1]:
      print 'Warning!'

    num_face_dice.append(numero)
 #   print 'numero da face do dados', num_face_dice

 # print 'tamanho do vetor para o numero da face', len(num_face_dice)

  for i in range(0,len(num_face_dice)):
    Sum = Sum + num_face_dice[i]
    
  Sum_vector.append(Sum)

 # print 'soma dos valores nas faces', Sum
 # print 'vetor que guarda a soma em todos os experimentos', Sum_vector

  Sum = 0
  num_face_dice = []

print min(Sum_vector), max(Sum_vector)

fig = plt.figure()

# the histogram of the data: numeros gerados, bins, normed = 1 => contagens normalizadas, normed = 0 nao normalizadas
m, bins, patches = plt.hist(Sum_vector, HistMax - HistMin + 1, normed=0, facecolor='green', alpha=0.75)

plt.xlabel('Numbers')
plt.ylabel('Number counts')
plt.title(r'$\mathrm{Histogram\ of\ the\ sum\ of\ the\ numbers\ in\ %d\ dice }\ $' % N)
plt.axis([HistMin-1, HistMax + 1, 0, 10*M/7.5])
plt.grid(True)

#plt.show()

fig.savefig('hist-dice.png', dpi=fig.dpi)
  
  





















