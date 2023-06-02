# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(mean, variance, x):
    return 0.5*(1 + math.erf((x-mean)/math.sqrt(2*variance)))

def prob(lower, upper):
    prob_upper = cdf(mean, std_dev**2, upper)
    prob_lower = cdf(mean, std_dev**2, lower)
    
    return prob_upper-prob_lower

mean, std_dev = list(map(int, input().split(" ")))
x1 = int(input())
x23 = int(input())

print(round((1 - cdf(mean, std_dev**2, x1))*100, 2))
print(round((1 - cdf(mean, std_dev**2, x23))*100, 2))
print(round((cdf(mean, std_dev**2, x23))*100, 2))