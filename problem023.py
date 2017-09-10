def sof(n):
    sum = 1
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            sum += i
            if i != n//i:

                sum += n//i

    return sum
l = []
t = int(input())
for e in range(12, 28124):
    if sof(e) > e:
        l.append(e)
for _ in range(t):
    n = int(input())

    if n<12:
        print("NO")
    elif n > 28123:
        print("YES")
    else:
        boo = False
        for e in l:
            if e < n:
                if n-e in l:
                    boo = True
                    break
        if boo:
            print("YES")
        else:
            print("NO")