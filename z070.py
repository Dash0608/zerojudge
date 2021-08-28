def expend(n):
    if n <= 1:
        return 1
    else:
        return expend(n-1) + expend(n-2)
while True:
    try:
        n = int(input())
        print(expend(n))
    except:
        break