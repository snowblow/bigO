#!/usr/bin/python3

def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

L1 = [5, 6, 7, 8]
L2 = [5, 6, 7, 8]
print(isSubset(L1, L2))
