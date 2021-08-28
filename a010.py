n = int(input())
i = 2
c = 0
t = 0
while n > 1:  
    c = 0
    if t:
        print('*',end=' ')
    while n%i == 0:#判斷i是否為n的餘數
        n //= i
        c += 1#i的次數
    if c >= 2:
        print(f'{i}^{c}',end=' ')
        t += 1
    elif c:
        print(f'{i}',end=' ')
        t += 1
    else:
        t = 0
    i += 1
print()
