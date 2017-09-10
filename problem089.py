def apndr(c, n):
    s = ""
    for i in range(n, 1 -1, -1):
        s = s + c
    return s

# Main
def roman(n):
    s = ""
    while n != 0:
        if n >= 1000:
            s = s + apndr("M", (n) // 1000)
            n = n % 1000
        else:
            if n >= 500:
                if n < 900:
                    s = s + "D"
                    s = s + apndr("C", (n - 500) // 100)
                else:
                    s = s + "CM"
            else:
                if n >= 100:
                    if n < 400:
                        s = s + apndr("C", n // 100)
                    else:
                        s = s + "CD"
                else:
                    if n >= 50:
                        if n < 90:
                            s = s + "L"
                            s = s + apndr("X", (n - 50) // 10)
                        else:
                            s = s + "XC"
                    else:
                        if n >= 10:
                            if n < 40:
                                s = s + apndr("X", n // 10)
                            else:
                                s = s + "XL"
                        else:
                            if n >= 5:
                                if n < 9:
                                    s = s + "V"
                                    s = s + apndr("I", n - 5)
                                else:
                                    s = s + "IX"
                            else:
                                if n < 4:
                                    s = s + apndr("I", n)
                                else:
                                    s = s + "IV"
                            n = 0
                    n = n % 10
            n = n % 100
    return s


t = int(input())
for _ in range(t):
    s = input()
    n = 0
    for e in s:
        if e == 'M':
            n += 1000
        elif e == 'D':
            n += 500
        elif e == 'C':
            n += 100
        elif e == 'L':
            n += 50
        elif e == 'X':
            n += 10
        elif e == 'V':
            n += 5
        elif e == 'I':
            n += 1
    print(roman(n))