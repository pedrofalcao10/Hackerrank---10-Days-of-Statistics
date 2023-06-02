import math

def cdf(mean, variance, x):
    return 0.5*(1 + math.erf((x-mean)/math.sqrt(2*variance)))

def prob(lower, upper):
    prob_upper = cdf(mean, std_dev**2, upper)
    prob_lower = cdf(mean, std_dev**2, lower)
    
    return prob_upper-prob_lower

mean, std_dev = list(map(int, input().split(" ")))
x = float(input())
range_lower, range_upper = list(map(int, input().split(" ")))

print(round(cdf(mean, std_dev**2, x), 3))
print(round(prob(range_lower, range_upper), 3))