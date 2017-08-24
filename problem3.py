r = int(input())
m = []
for i in range(r):
    m.append(input())
for n in m:
    n = int(n)
    j = 2

    large = 2
    while j * j <= n:
        while n % j == 0:

            large = j
            n = n// j

        j += 1
    if (n > large):
        print(n)
    else:
        print(large)
