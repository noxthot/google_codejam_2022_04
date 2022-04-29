import numpy as np
import os

DEBUG = False
READ_INPUT_FROM_FILE = True


if READ_INPUT_FROM_FILE:
    in_file = open(os.path.join("0_qualification", 'e3.in'))
    

def getNextInput():
    return in_file.readline() if READ_INPUT_FROM_FILE else input()
    

def getLongestStraight(n, s):
    s_sorted = s.copy()
    s_sorted.sort()
    l = 0

    for sides_die in s_sorted:
        if sides_die > l:
            l += 1

    return l


# Read input
T = int(getNextInput())  # nr Testcases

N = [None] * T  # nr of dice
S = [None] * T  # sides of dice

for i in range(T):
    N[i] = int(getNextInput())
    S[i] = [int(val) for val in getNextInput().split(" ")]

# Solve problem and output
for i in range(T):
    out = getLongestStraight(N[i], S[i])
    print(f"Case #{i + 1}: {out}")

if READ_INPUT_FROM_FILE:
    in_file.close()
