def base(n, b):
    s = ''
    while(n>=b):
        print(n)
        s = str(n%b)+s
        n = n//b
    return str(n % b)+s


n, b = input().split()

n = int(n)
b = int(b)
s = 0
for e in range(n):
    if str(e) == str(e)[::-1]:
        d = base(e, b)
        if str(d) == str(d)[::-1]:
            s += e
print(s)
