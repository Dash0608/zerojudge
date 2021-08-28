a = int(input())
l = list(map(int,input().split()))
w = -50
b = 500
l.sort()
for j in range(0,a):
    if j <= a-2 :
        print(l[j],end=' ')
    else:
        print(l[j])
    if l[j] < 60 and l[j] > w:
        w = l[j]
    if l[j] >= 60 and l[j] < b:
        b = l[j]
if w >= 0:
   print(w) 
else:
   print('best case')
if b <= 100:
   print(b) 
else:
   print('worst case')