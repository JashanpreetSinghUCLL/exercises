
from itertools import *

def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, n))

def primes():
    return (n for n in count(2) if is_prime(n))

