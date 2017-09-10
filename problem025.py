fib = [0 for i in range(5008)]
a, b = 1, 1
cnt = 1
while(len(str(b)) < 5000 + 7):
    a, b = b, a + b
    cnt += 1
    fib[len(str(b))] = cnt

for t in range(int(input())):
    print (fib[int(input()) - 1] + 2)