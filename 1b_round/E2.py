import numpy as np
import os

DEBUG = False
READ_INPUT_FROM_FILE = False


if READ_INPUT_FROM_FILE:
    in_file = open(os.path.join("1b_round", 'e2.in'))
    

def getNextInput():
    return in_file.readline() if READ_INPUT_FROM_FILE else input()
    

def getBestDecision(currPress, X, Xn):
    minX = min(X)
    maxX = max(X)

    leftScore = abs(minX - currPress) + (maxX - minX)
    rightScore = abs(maxX - currPress) + (maxX - minX)

    if np.size(Xn) > 0:
        minXn = min(Xn)
        maxXn = max(Xn)

        leftrightscore = leftScore + abs(maxX - maxXn)
        leftleftScore = leftScore + abs(maxX - minXn)
        rightrightscore = rightScore + abs(minX - maxXn)
        rightleftScore = rightScore + abs(minX - minXn)
        
        if np.argmin([leftrightscore, leftleftScore, rightrightscore, rightleftScore]) <= 1:
            addScore = leftScore
            newPress = maxX
        else:
            addScore = rightScore
            newPress = minX
    else:
        if leftScore < rightScore:
            addScore = leftScore
            newPress = maxX
        else:
            addScore = rightScore
            newPress = minX

    return newPress, addScore


def countButtonSwitches(N, _, X):
    currPress = 0
    sumScore = 0

    for j in range(N):
        Xn = X[j + 1] if j + 1 < N else []

        currPress, addScore = getBestDecision(currPress, X[j], Xn)
        sumScore += addScore

    return sumScore


# Read input
T = int(getNextInput())  # nr Testcases

N = [None] * T  # Rows
P = [None] * T  # Tires per client
X = [None] * T  # Pressures per Tire

for i in range(T):
    N[i], P[i] = [int(val) for val in getNextInput().split(" ")]
    X[i] = [None] * N[i]

    for j in range(N[i]):
        X[i][j] = [int(val) for val in getNextInput().split(" ")]

# Solve problem and output
for i in range(T):
    out = countButtonSwitches(N[i], P[i], X[i])
    print(f"Case #{i + 1}: {out}")

if READ_INPUT_FROM_FILE:
    in_file.close()
