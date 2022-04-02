#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name=list(s.split())

    final=[]

    for i in name:
        cap=i[0].upper()
        word=i.replace(i[0],cap)
        final.append(word)
    print(" ".join(final))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
