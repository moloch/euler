'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import unittest

def multiples_of_both(n, m, limit=10):
  result = []
  for x in range(limit):
    if x%n==0 or x%m==0:
      result.append(x)
  return result

class problem001Test(unittest.TestCase):
  
  def test_small(self):
    self.assertEqual(23, sum(multiples_of_both(3, 5, limit=10)))
    print sum(multiples_of_both(3,5, limit=1000))
