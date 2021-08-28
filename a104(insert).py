while True:
    try:
        a = int(input())
        l = list(map(int,input().split()))
        for i in range(1,a):
            if l[i] < l[i-1]:
                b = i
                c = l[i]
                while l[i] < l[b-1] and b > 0:
                    b -= 1  
                del l[i]
                l.insert(b,int(c))
        for i in l:
            print(i,end=' ')
        print()
    except:
        break