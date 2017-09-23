#!/usr/bin/python3

def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

print(addDigits("1234"))

def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

print(fact_iter(4))

