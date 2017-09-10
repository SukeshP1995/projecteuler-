t = int(input())

for _ in range(t):
    n = int(input())
    l = []

    for i in range(n):
        l.append(list(map(int, input().split())))
    r, c = 0, 0
    try:
        for r in range(n - 2, -1, -1):
            for c in range(0, r + 1):
                l[r][c] += max([l[r + 1][c], l[r + 1][c + 1]])
    except:
        pass

    print(l[0][0])