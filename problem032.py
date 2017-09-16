def check(s, n):
    if n == 4:
        if s == '1234':
            return True
        return False
    elif n == 5:
        if s == '12345':
            return True
        return False
    elif n == 6:
        if s == '123456':
            return True
        return False
    elif n == 7:
        if s == '1234567':
            return True
        return False
    elif n == 8:
        if s == '12345678':
            return True
        return False
    elif n == 9:
        if s == '123456789':
            return True
        return False

n = int(input())
l = []
su = 0
for i in range(100):
    if (''.join(sorted(list(str(i)))) == ''.join(sorted(set(list(str(i)))))) and '0' not in str(i):
        for j in range(10000):
            if ''.join(sorted(list(str(j)))) == ''.join(sorted(set(list(str(j))))) and '0' not in str(j):
                if ''.join(sorted(list(str(j)+str(i)))) == ''.join(sorted(set(list(str(i)+str(j))))):
                    if ''.join(sorted(list(str(j*i)))) == ''.join(sorted(set(list(str(i*j))))):
                        if ''.join(sorted(list(str(j) + str(i) + str(i*j)))) == ''.join(sorted(set(list(str(i) + str(j) + str(i*j))))) and '0' not in str(i*j):
                            s = ''.join(sorted(list(str(j) + str(i)+str(i*j))))

                            if check(s, n) and (i*j) not in l:
                                su += i*j

                                l.append(i*j)
print(su)