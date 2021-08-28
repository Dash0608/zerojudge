import math
while True:        
    try:   
        n = int(input())
        n2 = n
        l = 0
        i = 2
        c = 0
        while n>1:
            if  i>(math.sqrt(n2)):
                c = 1
                break
            while n%i==0:
                n //= i
                l+=i
            i+=1
        if l!=0:
            if c == 0:
                print(l)
            else:
                print(l+n)
        else:
            print(n)
    except:
        break