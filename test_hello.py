import unittest
import hello
import math

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(3, 4), 7)
        self.assertNotEqual(hello.add(3, 4), 1)

    def test_subtract(self):
        self.assertEqual(hello.sub(10, 6), 4)

    def test_multiply(self):
        self.assertEqual(hello.mul(2, 8), 16)

    #div, sqrt, power, log, exp

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertNotEqual(hello.sin(0), 1)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertAlmostEqual(hello.sin(1 + 2*math.pi()), 0.8414, 3)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
