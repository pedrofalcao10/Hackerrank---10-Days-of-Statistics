#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def mid(arr):
    if len(arr) % 2 == 0:
        return int((arr[(len(arr) // 2)-1] + arr[len(arr) // 2]) / 2)
    return arr[len(arr) // 2]

def quartiles(arr):
    arr = sorted(arr)
    q1 = mid(arr[ : len(arr) // 2 ])
    q2 = mid(arr)
    q3 = mid(arr[(len(arr) + 1) // 2 : ])
    return [q1, q2, q3]

def interQuartile(values, freqs):
    data = [val for val, freq in zip(values, freqs) for i in range(freq)]
    quarts = quartiles(data)
    print( float(quarts[2] - quarts[0]))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
