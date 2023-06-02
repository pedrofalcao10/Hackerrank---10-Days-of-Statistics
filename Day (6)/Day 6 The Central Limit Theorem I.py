# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(mean, variance, x):
    return 0.5*(1 + math.erf((x-mean)/math.sqrt(2*variance)))

max_weight = int(input())
num_boxes = int(input())
mean_weight = int(input())
std_dev = int(input())

mean = mean_weight*num_boxes
variance = num_boxes*std_dev**2

'''
9800
49
205
15
'''

print(round(cdf(mean, variance, max_weight), 4))