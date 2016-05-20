'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import unittest
from operator import mul

def smallest_divisor(n):
  x = n
  while True:
    if is_divisible_by_all(x, range(1,n+1)):
      return x
    x+=n


def is_divisible_by_all(x, _range):
  for n in _range:
    if x % n != 0:
      return False
  return True

class problem005Test(unittest.TestCase):

  def test_small(self):
    self.assertTrue(is_divisible_by_all(2520, range(1,10)))
    self.assertEqual(2520, smallest_divisor(10))
    print smallest_divisor(20)
