#!/usr/bin/env python

#
# write a function that
# takes an integer n
# and finds the nth prime
# your list of primes begins at 2.
#

def isprime(m): 
    for k in range(2, int(m**0.5 + 1)): 
        if m%k==0: 
            return False
    return True

def nthprime(n):
    '''receives an int and gives an int back'''
    primes = [k for k in range(2, n**4) if isprime(k)]
    return primes[n]
