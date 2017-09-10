n = int(input())
n = n-1
def rotates(e):
    r = e
    l = []
    e = e[1:]+e[0]
    l.append(int(e))
    while r != e:
        e = e[1:]+e[0]
        l.append(int(e))
    return l

l = [i for i in range(n+1)]
l3 = []
l2 = [True] * len(l)
for i in range(2, n+1):
    for j in range(i * i, n+1, i):
        l2[j] = False
    if l2[i]:
        if len(str(l[i])) == 1 or '0' not in str(l[i]) and '2' not in str(l[i]) and '4' not in str(l[i]) and '5' not in str(l[i]) and '6' not in str(l[i]) and '8' not in list(str(l[i])):
            l3.append(l[i])
l4 = l3[:]
for e in l4:
    pl = rotates(str(e))
    flag = 0

    for g in pl:

        if not l2[g]:
            l3.remove(e)
            break
print(sum(l3))
