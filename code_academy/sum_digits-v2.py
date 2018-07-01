#! /usr/bin/python

def digit_sum(n):
  sum = 0
  n = int(n)
  while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
  return sum

print 

num_input = raw_input("Digite um numero: ")

print 'Sum of the digits is:', digit_sum(num_input)

print
