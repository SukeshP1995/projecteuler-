def n2w0to19(n):

    if n == 0:
        return 'Zero'
    elif n == 1:
        return 'One'
    elif n == 2:
        return 'Two'
    elif n == 3:
        return 'Three'
    elif n == 4:
        return 'Four'
    elif n == 5:
        return 'Five'
    elif n == 6:
        return 'Six'
    elif n == 7:
        return 'Seven'
    elif n == 8:
        return 'Eight'
    elif n == 9:
        return 'Nine'
    elif n == 10:
        return 'Ten'
    elif n == 11:
        return 'Eleven'
    elif n == 12:
        return 'Twelve'
    elif n == 13:
        return 'Thirteen'
    elif n == 14:
        return 'Fourteen'
    elif n == 15:
        return 'Fifteen'
    elif n == 16:
        return 'Sixteen'
    elif n == 17:
        return 'Seventeen'
    elif n == 18:
        return 'Eighteen'
    elif n == 19:
        return 'Nineteen'

def n2w20to90(n):
    if n == 20:
        return 'Twenty'
    elif n == 30:
        return 'Thirty'
    elif n == 40:
        return 'Forty'
    elif n == 50:
        return 'Fifty'
    elif n == 60:
        return 'Sixty'
    elif n == 70:
        return 'Seventy'
    elif n == 80:
        return 'Eighty'
    elif n == 90:
        return 'Ninety'

def n2w10s(n):
    if n == 2:
        return 'Hundred'
    elif n == 3:
        return 'Thousand'
    elif n == 6:
        return 'Million'
    elif n == 9:
        return 'Billion'
    elif n == 12:
        return 'Trillion'

def n2wt(n):

    part1 = n//100

    s = ''
    flag = False
    if part1>=1:
        flag = True
        s += n2w0to19(part1)+' '+'Hundred'
    part2 = n%100
    if part2 >= 20:
        if flag:
            s += ' '
        temp = part2 - part2%10
        part2 = part2%10
        s += n2w20to90(temp)
        flag = True
    if part2>0:
        if flag:
            s+=' '
        s +=n2w0to19(part2)

    return s

t = int(input())
for i in range(t):
    n = int(input())
    s = ''
    part1 = n//10**12

    if part1>0:
        s = n2wt(part1)+' '+n2w10s(12)+' '
    n = n%(10**12)

    part2 = n//10**9
    if part2>0:
        s += n2wt(part2)+' '+n2w10s(9)+' '
    n = n%(10**9)


    part3 = n//10**6
    if part3>0:
        s += n2wt(part3)+' '+n2w10s(6)+' '
    n = n%(10**6)

    part4 = n//10**3
    if part4>0:
        s += n2wt(part4)+' '+n2w10s(3)+' '
    n = n%(10**3)
    part5 = n
    if part5>0:
        s += n2wt(part5)
    print(s)