while True:    
    try:
        l = [0] * 46
        l[0] = 1
        l[1] = 1
        n = int(input())
        for i in range(2,n+1):
            l[i] = l[i-1] + l[i-2]
        print(l[n])
    except:
        break
#def rec(n):
    
    #return 