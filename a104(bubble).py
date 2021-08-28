while True:
    try:
        a = int(input())
        l = list(map(int,input().split()))
        for i in range(a):
            c = 0
            for j in range(a-1):  
                if l[j] > l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]
                    c += 1
            if c == 0:
                break
        for i in range(len(l)):
            print(l[i],end=' ')
        print()
    except:
        break