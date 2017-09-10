n = int(input())-1
l = [i for i in range(n + 1)]
l3 = []
cnt = 0
l2 = [True] * len(l)
l5 = []
for i in range(2, n + 1):
    for j in range(i * i, n + 1, i):
        l2[j] = False
    if l2[i]:
        l5.append(l[i])
        t = l[i]
        flag = True
        if t > 9:
            t = t // 10
            while t != 0:

                if t not in l3:
                    flag = False
                    break
                t = t//10

        if flag:
            l3.append(l[i])

l4 = l3[5:]
for e in l4:
    t1 = str(e)[1:]

    while t1!='':
        t = int(t1)
        if t not in l5:

            l3.remove(e)
            break
        if t<9:
            break
        t1 = str(t)[1:]
print(sum(l3)-17)