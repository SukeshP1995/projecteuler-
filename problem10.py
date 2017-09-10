import math

d = {}


def sieve(n):
    sum1 = 0
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            sum1 = sum1 + i
            for j in range(i * i, n + 1, i):
                primes[j] = False
        if i in d:
            pass
        else:
            d[i] = sum1


a = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a.append(n)
sieve(max(a))

for i in a:
    print(d[i])