#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mid(arr):
    print(arr)
    if len(arr) % 2 == 0:
        return int((arr[(len(arr) // 2)-1] + arr[len(arr) // 2])/ 2)
    return arr[len(arr) // 2]

def quartiles(arr):
    arr = sorted(arr)
    q1 = mid(arr[ : len(arr) // 2 ])
    q2 = mid(arr)
    q3 = mid(arr[(len(arr) + 1) // 2 : ])
    return [q1, q2, q3]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
