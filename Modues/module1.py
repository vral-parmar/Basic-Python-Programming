from module import k, print_parameters
from math import factorial
n = 5.0
def combiations(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)