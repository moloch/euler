'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import unittest

def sieve(n):
  numbers = [x for x in range(2,n+1)]
  primes = []
  while len(numbers) > 0:
    actual = numbers[0]
    primes.append(actual)
    numbers = numbers[1:]
    for x in numbers:
      if x%actual == 0:
        numbers.remove(x)
  return primes

class problem007Test(unittest.TestCase):

  def test_small(self):
    self.assertEqual([2,3,5,7,11,13], sieve(14))
    primes = sieve(130000)
    print primes[10000]
