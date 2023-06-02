# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def combination(n, x):
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

def binomial_distribution(x, n, p):
    return combination(n, x)*pow(p, x)*pow(1-p, n-x)

perc, size = list(map(float, input().split(" "))) # 12.0 10.0
perc /= 100 # 0.12
size = int(size) # 10

# no more than 3 rejects
print(round(sum([binomial_distribution(i, size, perc) for i in range(0, 3)]), 3))
# at least 2 rejects
print(round(sum([binomial_distribution(i, size, perc) for i in range(2, 11)]), 3))
