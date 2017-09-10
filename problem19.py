def grg(q, m, k, j):
    a = 13*(m+1)//5
    b = k//4+j//4
    h = q + a + k + b + 5*j
    return h % 7
t = int(input())

for _ in range(t):
    d1, m1, y1 = map(int, input().split())
    d2, m2, y2 = map(int, input().split())
    s = 0
    if d1 != 1:
        d1 = 1
        m1 += 1
        if m1 == 13:
            y1 += 1
            m1 = 1

    if d2 != 1:
        d2 = 1

    i = m1
    p = y1

    while p <= y2:

        q = 1
        m = i
        if m < 3:
            m += 12
        p1 = p
        if m == 13 or m == 14:
            p1 = p - 1

        k = p1 % 100
        j = p1//100
        d = grg(q, m, k, j) % 7
        if d == 1:

            s += 1

        i += 1

        if i == 13:

            i = 1
            p += 1
        if i > m2 and p >= y2:
            break

    print(s)