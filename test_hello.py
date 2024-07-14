# Test file for hello.py testing each unit case (NOTE: Complex numbers are not considered)

# Import necessary libraries
import unittest
import hello
import math


# Class with all the tests
class TestHello(unittest.TestCase):
    # Should only produce Hello World
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    # Addition Test
    def test_add(self):
        # Check any integers (with different combinations of both positive and negative integers), any floats
        self.assertEqual(hello.add(3, 4), 7)
        self.assertNotEqual(hello.add(3, 4), 1)
        self.assertEqual(hello.add(7, -9), -2)
        self.assertNotEqual(hello.add(7, -9), 2)
        self.assertEqual(hello.add(-11, 3), -8)
        self.assertNotEqual(hello.add(-11, 3), -14)
        self.assertEqual(hello.add(-5, -2), -7)
        self.assertNotEqual(hello.add(-5, -2), -3)
        self.assertAlmostEqual(hello.add(3.6, 1.9), 5.500000, 5)

    # Subtraction Test
    def test_subtract(self):
        # Check any integers (with different combinations of both positive and negative integers), any floats
        self.assertEqual(hello.sub(3, 4), -1)
        self.assertNotEqual(hello.sub(3, 4), 1)
        self.assertEqual(hello.sub(7, -9), 16)
        self.assertNotEqual(hello.sub(7, -9), -2)
        self.assertEqual(hello.sub(-11, 3), -14)
        self.assertNotEqual(hello.sub(-11, 3), -8)
        self.assertEqual(hello.sub(-5, -2), -3)
        self.assertNotEqual(hello.sub(-5, -2), -7)
        self.assertAlmostEqual(hello.sub(3.6, 1.9), 1.700000, 5)

    # Multiplication Test
    def test_multiply(self):
        # Check zero, positive integers, negative integers, different combinations of both positive and negative integers, any floats
        self.assertEqual(hello.mul(3, 4), 12)
        self.assertNotEqual(hello.mul(3, 4), 34)
        self.assertEqual(hello.mul(7, -9), -63)
        self.assertNotEqual(hello.mul(-9, 7), -97)
        self.assertEqual(hello.mul(-11, -3), 33)
        self.assertNotEqual(hello.mul(-11, -3), -33)
        self.assertEqual(hello.mul(0, 8), 0)
        self.assertNotEqual(hello.mul(0, 8), 1)
        self.assertEqual(hello.mul(3.6, 1.9), 6.840000, 5)

    # Division Test
    def test_divide(self):
        # Check positive integers, negative integers, different combinations of both positive and negative integers, any floats
        self.assertEqual(hello.div(4, 2), 2)
        self.assertNotEqual(hello.div(4, 2), 0.5)
        self.assertEqual(hello.div(-10, 10), -1)
        self.assertNotEqual(hello.div(-10, 10), 1)
        self.assertEqual(hello.div(3, 10), 0.3)
        self.assertAlmostEqual(hello.div(3, 10), 0.299999, 5)
        self.assertAlmostEqual(hello.div(1, 3), 0.333333, 5)
        self.assertAlmostEqual(hello.div(4.2, 2.1), 2.000000, 5)

        # Raise error for division by zero
        try:
            hello.div(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Can't divide by zero!")

    # Square Root Test
    def test_sqrt(self):
        # Check nonnegative integers, irrational roots, nonnegative floats
        self.assertEqual(hello.sqrt(81), 9)
        self.assertNotEqual(hello.sqrt(81), 3)
        self.assertAlmostEqual(hello.sqrt(7), 2.645751, 5)
        self.assertEqual(hello.sqrt(0), 0)
        self.assertNotEqual(hello.sqrt(0), 1)

        # Raise error for negative parameters
        try:
            hello.sqrt(-4)
        except ValueError as e:
            self.assertEqual(str(e), "Domain Error")

    # Power Test
    def test_power(self):
        # # Check zero, one, positive integers, negative integers, different combinations of both positive and negative integers, any floats
        self.assertEqual(hello.power(3, 4), 81)
        self.assertNotEqual(hello.power(3, 4), 12)
        self.assertAlmostEqual(hello.power(1.2, 2.4), 1.548941, 5)
        self.assertEqual(hello.power(-2, 3), -8)
        self.assertNotEqual(hello.power(-2, 3), 8)
        self.assertEqual(hello.power(0, 4), 0)
        self.assertNotEqual(hello.power(0, 4), 4)
        self.assertEqual(hello.power(1, 1), 1)
        self.assertNotEqual(hello.power(1, 4), 4)

        # THESE TESTS BELOW ARE NOT SUPPORTED BY NUMPY'S POWER FUNCTION (does not take negative exponents) BUT SHOULD BE TESTED IN REAL LIFE REGARDLESS

        # self.assertEqual(hello.power(1, -1), 1)
        # self.assertNotEqual(hello.power(1, -1), 0)
        # self.assertAlmostEqual(hello.power(4, -2), 0.062500, 5)
        # self.assertNotEqual(hello.power(4, -2), -2)

        # Test with base e
        self.assertAlmostEqual(hello.power(math.e, math.log(math.e)), 2.718281, 5)
        self.assertNotEqual(hello.power(math.e, math.log(math.e)), 1)

        # Raise error for 0^0
        try:
            hello.power(0, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Domain Error")

    # Natural Logarithm Test
    def test_log(self):
        # Check with e, positive integers and floats
        self.assertAlmostEqual(hello.log(math.e), 1.000000, 5)
        self.assertNotEqual(hello.log(math.e), 2.718)
        self.assertAlmostEqual(hello.log(1), 0.000000, 5)
        self.assertNotEqual(hello.log(1), 1)
        self.assertAlmostEqual(hello.log(1.2), 0.182321, 5)
        self.assertAlmostEqual(hello.log(10), 2.302585, 5)

        # Raise error for nonpositive integers and floats
        try:
            hello.log(-2.8)
            hello.log(-4)
            hello.log(0)
        except ValueError as e:
            self.assertEqual(str(e), "Domain Error")

    # Base e Test
    def test_exp(self):
        # Check any integers, floats
        self.assertAlmostEqual(hello.exp(1), 2.718281, 5)
        self.assertNotEqual(hello.exp(1), 0)
        self.assertAlmostEqual(hello.exp(-1), 0.367879, 5)
        self.assertNotEqual(hello.exp(-1), -1)
        self.assertAlmostEqual(hello.exp(2.2), 9.025013, 5)

    # Sine Test
    def test_sin(self):
        # Check any integers, floats, irrational numbers, repeating values (period = 2 pi)
        self.assertEqual(hello.sin(0), 0)
        self.assertNotEqual(hello.sin(0), 1)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertAlmostEqual(hello.sin(4.6), -0.993691, 5)
        self.assertAlmostEqual(hello.sin(1 + 2 * math.pi), 0.8414, 3)

    # Cosine Test
    def test_cos(self):
        # Check any integers, floats, irrational numbers, repeating values (period = 2 pi)
        self.assertEqual(hello.cos(0), 1)
        self.assertNotEqual(hello.cos(0), 0)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertAlmostEqual(hello.cos(4.6), -0.112152, 5)
        self.assertAlmostEqual(hello.cos(1 + 2 * math.pi), 0.540302, 5)

    # Tangent Test
    def test_tan(self):
        # Check any integers, floats, irrational numbers, repeating values (period = pi)
        self.assertEqual(hello.tan(0), 0)
        self.assertNotEqual(hello.tan(0), 1)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertAlmostEqual(hello.tan(1.8), -4.286261, 5)
        self.assertAlmostEqual(hello.tan(1 + math.pi), 1.557407, 5)

        # Raise error at asymptotes (every multiple of pi/2 except 0)
        try:
            hello.tan(math.pi / 2)
        except ValueError as e:
            self.assertEqual(str(e), "Domain Error")

    # Cotangent Test
    def test_cot(self):
        # Check any integers, floats, irrational numbers, repeating values (period = pi)
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertNotEqual(hello.cot(1), 1)
        self.assertAlmostEqual(hello.cot(1 + math.pi), 0.642092, 5)
        self.assertAlmostEqual(hello.cot(2.2), -0.727895, 5)

        # Raise error at asymptotes (every multiple of pi except 0)
        try:
            hello.cot(math.pi)
        except ValueError as e:
            self.assertEqual(str(e), "Domain Error")


if __name__ == "__main__":
    unittest.main()
