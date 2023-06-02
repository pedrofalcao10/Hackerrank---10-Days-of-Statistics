# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def combination(n, x):
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

def poisson_distribution(k, lamb):
    return pow(lamb, k)*pow(math.e, -lamb)/math.factorial(k)

A, B = list(map(float, input().split(" ")))

cost_A = 160 + 40*(A + A**2)
cost_B = 128 + 40*(B + B**2)

print(round(cost_A, 3))
print(round(cost_B, 3))
