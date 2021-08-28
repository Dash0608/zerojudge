l = list()
n = int(input())
de = 0
for i in range(n):
    l.append(tuple(map(int,input().split())))
l.sort()
st = l[0][0]
fn = l[0][1]
for i in range(1,n):
    if (fn - l[i][0]) < 0:
        de += (fn - l[i][0])
    if l[i][1] > fn:
        fn = l[i][1]
print(fn-st+de)                