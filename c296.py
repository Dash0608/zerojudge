n,m,k = list(map(int,input().split()))
b = 0
l = list()
for i in range(1,n+1):
    l.append(i)
for j in range(k):
    rem = len(l)
    for k in range(m-1):
        if b >= rem-1:
            b = 0
        else:
            b += 1
    '''print(b)
    print(l)'''
    del l[b]
    rem -= 1
    b -= 1
    if b >= rem-1:
        b = 0
    else:
        b += 1
    '''print(b)
    print(l)'''
print(l[b])