# This is the hello.py file which contains functions for performing various mathematical operations

# Import necessary library
import numpy as np


# Simple hello world function
def hello():
    return "Hello, world!"


# ALL MATHEMATICAL FUNCTIONS HAVE PARAMETERS THAT ARE FORCED TO BE INITIALIZED AS INTEGERS AND/OR FLOATS (COMPLEX NUMBERS ARE NOT CONSIDERED)


# Addition
def add(a: int | float, b: int | float):
    return a + b


# Subtraction
def sub(a: int | float, b: int | float):
    return a - b


# Multiplication
def mul(a: int | float, b: int | float):
    return a * b


# Division
def div(a: int | float, b: int | float):
    if b == 0:
        raise ValueError("Can't divide by zero!")

    return a / b


# Square Root
def sqrt(a: int | float):
    if a < 0:
        raise ValueError("Domain Error")

    return np.sqrt(a)


# Power Function
def power(a: int | float, b: int | float):
    if a == 0 and b == 0:
        raise ValueError("Domain Error")

    return np.power(a, b)


# Natural Logarithm
def log(a: int | float):
    if a <= 0:
        raise ValueError("Domain Error")

    return np.log(a)


# Base e
def exp(a: int | float):
    return np.exp(a)


# Sine
def sin(a: int | float):
    return np.sin(a)


# Cosine
def cos(a: int | float):
    return np.cos(a)


# Tangent
def tan(a: int | float):
    if a % (np.pi / 2) == 0 and a != 0:
        raise ValueError("Domain Error")

    return np.tan(a)


# Cotangent
def cot(a: int | float):
    if a % (np.pi) == 0:
        raise ValueError("Domain Error")

    return 1 / np.tan(a)


def __main__():
    hello()


if __name__ == "__main__":
    __main__()
