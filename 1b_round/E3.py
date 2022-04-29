import numpy as np

dbRecord = np.random.rand(8) > 0.5

def permRandom(dbRecord, inRecord):
    r = np.random.randint(8)
    permRec = np.hstack([dbRecord[-r:], dbRecord[:-r]])

    return permRec ^ inRecord
