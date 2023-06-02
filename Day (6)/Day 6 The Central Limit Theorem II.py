# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(mean, variance, x):
    return 0.5*(1 + math.erf((x-mean)/math.sqrt(2*variance)))

tickets_available = int(input())
num_buyers = int(input())
mean_purchased = float(input())
std_dev = float(input())

mean = mean_purchased*num_buyers
variance = num_buyers*std_dev**2

print(round(cdf(mean, variance, tickets_available), 4))
