t = int(input())
for i in range(t):
    n = int(input())
    prod = 1
    j = 1
    for j in range(1, n + 1):
        prod *= j

    s = sum(list(map(int,list(str(prod)))))
    print(s)