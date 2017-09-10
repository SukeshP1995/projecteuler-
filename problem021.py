from math import log10
def sot(n):
    sum = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:

            sum += i
            if i != n/i and n/i != n:

                sum += n/i

    return int(sum)

l = [i for i in range(1, 100000)]

t = int(input())
na = []
for _ in range(t):
    na = int(input())
    l1 = []
    for e in l[:]:
        if e>na:
            break

        if sot(sot(e)) == e and sot(e) != e:
            l1.append(e)
        else:
            l.remove(e)


    print(sum(l1))