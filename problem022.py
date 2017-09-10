t = int(input())
a = []
for _ in range(t):
    a.append(input())
a.sort()
def asc(e):
    print(ord(e)-64)
    return ord(e)-64
q = int(input())
for _ in range(q):
    s = input()
    su = sum(list(map(asc, list(s))))
    print(su*(a.index(s)))