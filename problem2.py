m = int(input())
j = 1
for i in range(m):
    n = int(input())
    a = 0
    b = 2
    summ = a+b
    while True:
            c = a + 4*b
            if c>=n:
                break
            a,b = b,c
            summ += c
            j += 1          
    print(summ)