while True:
    try:
        a = [0] * 101
        r = list()
        c = int(input())
        l = list()
        for i in range(c+1):
            r.append(a.copy())
        for i in range(c):
            t = list(map(int,input().split()))
            l.append(t)
        for i in range(1,c+1):
            for j in range(1,101):
                    if l[i-1][0] <= j:
                        temp = max(r[i-1][j],r[i-1][j-l[i-1][0]]+l[i-1][1])
                        r[i][j] = temp
                        #del l[l.index(l[i])]
                    else:
                        r[i][j] = r[i-1][j]
        print(r[c-1][100])
        print(r)
    except:
        break