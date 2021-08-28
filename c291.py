n = int(input())
l = list()
a = list(map(int,input().split()))
r = []
c = 0
for i in range(n):
    l.append(i)
for i in range(n):
    if (l[i] not in r) and (a[i] not in r):
        c += 1
        r.append(l[i])
        r.append(a[i])
    #elif 
print(c)