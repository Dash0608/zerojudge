a = list(map(int,input().split()))
b = int(input())
count = 0
for i in range(0,b):
    l = list(map(int,input().split()))
    c = 0
    d = 0
    for j in range(0,len(l)):
        if l[j] == a[0]:
            c += 1
        if l[j] == -a[0]:
            c -= 1
        if l[j] == a[1]:
            d += 1
        if l[j] == -a[1]:
            d -= 1
    if c > 0 and d > 0:
        count += 1
print(count)