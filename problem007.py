l = [i for i in range(200000 + 1)]
l3 = []
cnt = 0
l2 = [True] * len(l)

for i in range(2, 200000 + 1):
    for j in range(i * i, 200000 + 1, i):
        l2[j] = False
    if l2[i]:
        l3.append(l[i])

u = int(input())

for t in range(u):
    print(l3[int(input()) - 1])