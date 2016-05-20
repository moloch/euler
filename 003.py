"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import unittest

def is_prime(n):
  for x in range(2, n):
    if n % x == 0:
      return False
  return True


def prime_factors(n):
  factors = []
  x = 2
  while x <= n:
    if n % x == 0 and is_prime(x):
      factors.append(x)
      n = n / x
      x = 2
    x += 1
  return factors


class problem003Test(unittest.TestCase):

  def test_small(self):
    for n in [5,7,13,29]:
      self.assertTrue(is_prime(n))

    self.assertEqual([5,7,13,29], prime_factors(13195))
    print prime_factors(600851475143L)