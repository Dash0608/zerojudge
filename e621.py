while True:        
    try:        
        n = int(input())
        for i in range(n):
            a,b,c = list(map(int,input().split()))
            l = list()
            for j in range(a+1,b):
                if j%c != 0:
                    l.append(j)
            if len(l) != 0:
                for j in l:
                    print(j,end=' ')
            else:
                print('No free parking spaces.')
            print()
    except:
        break