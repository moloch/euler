'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import unittest

def is_palindromic(n):
  return str(n) == str(n)[::-1]

def largest_palindromic_product(digits):
  largest = 0
  a = b = limit = int('9'*digits)
  while a >= int('1'*digits) and b >= int('1'*digits):
    if is_palindromic(a*b):
      largest = a*b if a*b > largest else largest
    if b > int('1'*digits):
      b-=1
    else:
      a = b = a-1
  return largest

class problem004Test(unittest.TestCase):

  def test_small(self):
    self.assertTrue(is_palindromic(9009))
    self.assertEqual(9009, largest_palindromic_product(2))
    print largest_palindromic_product(3)
