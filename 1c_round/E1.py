import numpy as np
import os

DEBUG = False
READ_INPUT_FROM_FILE = False


if READ_INPUT_FROM_FILE:
    in_file = open(os.path.join("1c_round", 'e1.in'))
    

def getNextInput():
    return in_file.readline() if READ_INPUT_FROM_FILE else input()


def isTowerValid(S):
    foundLetters = set()

    for idx in range(len(S)):
        if (S[idx] in foundLetters) and (idx > 0) and (S[idx - 1] != S[idx]):
            return False
        
        foundLetters.add(S[idx])
    
    return True


def mergeConstantTowers(Ss):
    constantTowersIdx = [idx for idx in range(len(Ss)) if Ss[idx][0] == Ss[idx][-1]]
    otherTowers = [Ss[idx] for idx in range(len(Ss)) if idx not in constantTowersIdx]

    for idx in constantTowersIdx:
        appendedTower = False
        tower = Ss[idx]
        fl = tower[0]

        for idxOther in range(len(otherTowers)):
            if fl == otherTowers[idxOther][0]:
                otherTowers[idxOther] = tower + otherTowers[idxOther]
                appendedTower = True
                break
            elif fl == otherTowers[idxOther][-1]:
                otherTowers[idxOther] += tower
                appendedTower = True
                break

        if not appendedTower:
            otherTowers.append(tower)

    return otherTowers



def getSupertower(_, Ss):
    Ss = mergeConstantTowers(Ss)
    DEBUG and print(Ss)

    firstLetters = [S[0] for S in Ss]
    lastLetters = [S[-1] for S in Ss]

    availTowers = list(range(len(Ss)))
    
    #countFirstLetters = {s : 0 for s in firstLetters}

    #for letter in firstLetters:
    #    countFirstLetters[letter] += 1

    ret = ""

    while len(availTowers) > 0:
        #print(availTowers, flush=True)
        towerAdded = False
        lastAvailLetters = [lastLetters[i] for i in availTowers]

        for idx in availTowers:
            if ret == "" or ret[-1] == firstLetters[idx]:
                if firstLetters[idx] not in lastAvailLetters:
                    ret += Ss[idx]
                    availTowers.remove(idx)
                    towerAdded = True
                    break
        
        if not towerAdded:
            ret += Ss[availTowers.pop()]

    if not isTowerValid(ret):
        ret = "IMPOSSIBLE"

    return ret


# Read input
T = int(getNextInput())  # nr Testcases

N = [None] * T  # Number of Towers
Ss = [None] * T  # Towers

for i in range(T):
    N[i] = int(getNextInput())
    Ss[i] = [str.strip(tower) for tower in getNextInput().split(" ")]

# Solve problem and output
for i in range(T):
    out = getSupertower(N[i], Ss[i])
    print(f"Case #{i + 1}: {out}")

if READ_INPUT_FROM_FILE:
    in_file.close()
