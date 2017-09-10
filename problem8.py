from functools import reduce

t = int(input().strip())
for a0 in range(t):
    i = 0
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    l = []
    r = []
    while len(num[i:i + k]) >= k:
        l.append(num[i:i + k])
        i = i + 1
    for k in l:
        t = list(map(int, list(k)))
        r.append(reduce(lambda x, y: x * y, t))

    print(max(r))

