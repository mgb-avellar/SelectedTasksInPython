#! /usr/bin/python

def is_prime(x):
  if x < 2:
    return False
  elif x == 2:
    return True
  else:
    for n in range(2,x):
      if x % n == 0:
	return False
    return True


print 

num_input = int(raw_input("Digite um numero: "))

print 'The number %s is prime:' % num_input, is_prime(num_input)

print
