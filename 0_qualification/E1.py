import numpy as np
import os

DEBUG = False
READ_INPUT_FROM_FILE = False


if READ_INPUT_FROM_FILE:
    in_file = open(os.path.join("0_qualification", 'e1.in'))
    

def getNextInput():
    return in_file.readline() if READ_INPUT_FROM_FILE else input()
    

def drawPunchCard(nr_rows, nr_cols):
    out = ".." + "".join(["+-" for _ in range(nr_cols - 1)]) + "+\n"
    out += ".." + "".join(["|." for _ in range(nr_cols - 1)]) + "|\n"

    hline = "".join(["+-" for _ in range(nr_cols)]) + "+\n"
    cellline = "".join(["|." for _ in range(nr_cols)]) + "|\n"

    for _ in range(nr_rows - 1):
        out += hline
        out += cellline
    
    out += hline[:-1]

    return out


# Read input
T = int(getNextInput())  # nr Testcases

R = [None] * T  # Rows
C = [None] * T  # Cols

for i in range(T):
    R[i], C[i] = [int(val) for val in getNextInput().split(" ")]

# Solve problem and output
for i in range(T):
    out = drawPunchCard(R[i], C[i])
    print(f"Case #{i + 1}:")
    print(out)

if READ_INPUT_FROM_FILE:
    in_file.close()
