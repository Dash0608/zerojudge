while True:  
    try:  
        a = input()
        o = 0 
        e = 0
        for i in range(len(a)//2):#偶數位
            e += int(a[2*i+1])
        for i in range(len(a)-len(a)//2):
            o += int(a[2*i])
        print(abs(e-o))
    except:
        break