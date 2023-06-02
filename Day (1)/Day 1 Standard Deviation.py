#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)
    
    population_variance = 0

    for i in range(len(arr)):
        population_variance += (arr[i] - mean)**2

    std_Dev = (population_variance/len(arr))**0.5

    print(round(std_Dev, 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
