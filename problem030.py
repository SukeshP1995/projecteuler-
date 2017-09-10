n = int(input())
s = 0
def pow(a):
    return a**n

for i in range(100,600000):
    l = list(map(int,list(str(i))))
    if i == sum(list(map(pow,l))):
        s+=i

print(s)