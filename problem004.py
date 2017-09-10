t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maxx = 0
    for i in range(999,99,-1):
        for j in range(999,i-1,-1):
            mul = i*j
            if mul > n: continue
            if mul<maxx : break
            
            if str(mul) == str(mul)[::-1] and mul < n:
                maxx = mul
    print(maxx)