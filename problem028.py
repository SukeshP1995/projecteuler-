import math
t = int(input())
for _ in range(t):
    n = int(input())
    i = n//2
    s = (((16*i**3)+(30*i**2)+(26*i)+3)//3)%(10**9+7)
    print(s)