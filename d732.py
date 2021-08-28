n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
ans = list(map(int,input().split()))
for i in range(k):
        low = 0
        high = len(l)-1  
        m = (low+high)//2 
        while True:
            if high < low:
                print(0)
                break
            m = (low+high)//2                      
            if l[m] > ans[i]:
                high = m-1
            elif l[m]< ans[i]:
                low = m+1
            elif l[m] == ans[i]:
                print(l.index(l[m])+1)
                break
