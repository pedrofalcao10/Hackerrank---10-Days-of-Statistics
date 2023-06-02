# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def combination(n, x):
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

def poisson_distribution(k, lamb):
    return pow(lamb, k)*pow(math.e, -lamb)/math.factorial(k)

mean = float(input())
value = int(input())

print(round(poisson_distribution(value, mean), 3))