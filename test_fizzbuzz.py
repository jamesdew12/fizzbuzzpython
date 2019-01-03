import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_Fizz(self):
       self.assertEqual(fizzbuzz(1), 1)
       self.assertEqual(fizzbuzz(2), 2)
       self.assertEqual(fizzbuzz(3), "Fizz")
       self.assertEqual(fizzbuzz(4), 4)
       self.assertEqual(fizzbuzz(5), "Buzz")
       self.assertEqual(fizzbuzz(6), "Fizz")
       self.assertEqual(fizzbuzz(7), 7)
       self.assertEqual(fizzbuzz(8), 8)
       self.assertEqual(fizzbuzz(9), "Fizz")
       self.assertEqual(fizzbuzz(10), "Buzz")
       self.assertEqual(fizzbuzz(11), 11)
       self.assertEqual(fizzbuzz(12), "Fizz")
       self.assertEqual(fizzbuzz(13), 13)
       self.assertEqual(fizzbuzz(14), 14)
       self.assertEqual(fizzbuzz(15), "FizzBuzz")
       self.assertEqual(fizzbuzz(17), 17)
       self.assertEqual(fizzbuzz(18), "Fizz")
       self.assertEqual(fizzbuzz(19), 19)
       self.assertEqual(fizzbuzz(20), "Buzz")







if __name__ == '__main__':
    unittest.main()
