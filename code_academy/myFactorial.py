#! /usr/bin/python

def myFactorial(n):
  fac_mult = 1
  n = int(n)
  i = 1
  while i <= n:
    fac_mult = fac_mult * i
    i += 1
  return fac_mult

print 

num_input = raw_input("Digite um numero: ")

print 'The factorial is:', myFactorial(num_input)

print
