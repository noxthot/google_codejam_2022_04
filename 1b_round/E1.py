import numpy as np
import os

DEBUG = True
READ_INPUT_FROM_FILE = True


if READ_INPUT_FROM_FILE:
    in_file = open(os.path.join("1b_round", 'e1.in'))
    

def getNextInput():
    return in_file.readline() if READ_INPUT_FROM_FILE else input()
    

def countLostScore(D, val):
    return np.sum(np.array(D) < val)


def countMax(_, D):
    lastVal = float('-inf')
    cnt = 0

    while len(D) > 0:
        DEBUG and print(f"Length of D: {len(D)}")
        DEBUG and print(D)
        
        if countLostScore(D, D[0]) < countLostScore(D, D[-1]):
            # take left
            val = D.pop(0)
        else:
            val = D.pop()

        DEBUG and print(f"Remove {val}. New D: {D}")
        
        if val >= lastVal:
            cnt += 1
            lastVal = val
            DEBUG and print(f"add score: {cnt}")

    return cnt


# Read input
T = int(getNextInput())  # nr Testcases

N = [None] * T  # Rows
D = [None] * T  # Cols

for i in range(T):
    N[i] = int(getNextInput())
    D[i] = [int(val) for val in getNextInput().split(" ")]

# Solve problem and output
for i in range(T):
    out = countMax(N[i], D[i])
    print(f"Case #{i + 1}: {out}")

if READ_INPUT_FROM_FILE:
    in_file.close()
