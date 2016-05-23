# -*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''
import unittest

def sum_of_the_squares(numbers):
  return sum(x**2 for x in numbers)

def square_of_the_sum(numbers):
  return sum(numbers)**2

class problem006Test(unittest.TestCase):

  def test_small(self):
    self.assertEqual(385, sum_of_the_squares(range(1,10+1)))
    self.assertEqual(3025, square_of_the_sum(range(1,10+1)))
    print square_of_the_sum(range(1,100+1)) - sum_of_the_squares(range(1,100+1))
