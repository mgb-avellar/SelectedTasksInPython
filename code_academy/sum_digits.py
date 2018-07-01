#! /usr/bin/python

def digit_sum(n):
  num_str = str(n)
  sum = 0
  for digit in num_str:
    num_int_conversion = int(digit)
    sum += num_int_conversion
  return sum

print 

num_input = raw_input("Digite um numero: ")

print 'Sum of the digits is:', digit_sum(num_input)

print
