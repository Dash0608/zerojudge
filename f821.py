ans,n = input().split()
n = int(n)
for i in range(n):
    temp = input()
    a = 0
    b = 0
    for j in range(len(temp)):
        if temp[j] == ans[j]:
            a += 1
        elif temp[j] in ans:
            b += 1
    print(f'{a}A{b}B')