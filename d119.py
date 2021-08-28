while True:
    try:
        n = list(map(int,input().split()))
        l = [0] * (sum(n)+1)
        r = list()
        c = (1,5,10,20,50,100,200,500,1000,2000)
        rep = 0
        ans = 0
        r.append([1] * (sum(n)+1))
        for i in range(9):
            r.append(l.copy())
            r[i+1][0] = 1
        for i in range(10):
            if sum(n) > c[i]:
                rep += 1
            else:
                break
        for i in range(1,rep+1):
            for j in range(1,sum(n)+1):
                if j-c[i] < 0:
                    r[i][j] = r[i-1][j]
                else:
                    m = 0
                    while j-(m*c[i]) >= 0:
                        r[i][j] += r[i-1][j-(m*c[i])]
                        m += 1
        print(r[rep][len(r[i])-1]-1)
    except:
        break