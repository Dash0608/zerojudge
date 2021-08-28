while True:
    try:
        n,k = list(map(int,input().split()))
        p = list(map(int,input().split()))
        p.sort()
        r = list()
        #a = p.pop(p.index(k))
       # for i in range(len(p)-1):
       #     r.append(abs(a-p[i]))
       # r.sort()
        print(p[len(p)-1]-p[0])
    except:
        break

    