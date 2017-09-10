t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    maxp = -1
    for a in range(1,n//3):
        b = (n**2-2*a*n)//(2*n-2*a)
        c = n - a - b
        if c**2 == a**2 + b**2 and a <b and b <c:
            prod = a*b*c
            if prod > maxp:
                maxp = prod
    print(int(maxp))