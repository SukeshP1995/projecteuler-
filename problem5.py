#!/bin/python3
import functools
import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return functools.reduce(lcm, args)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lcmm(*range(1, n + 1)))

