while True:
    try:                
        n = int(input())
        i = 1
        ans = 0
        c = 0
        while True:
            for j in range(4):
                c += i
                ans +=1
                if c >= n:
                    break
            if c >= n:
                    break
            ans = 0
            i += 1  
        if ans == 1:
            print('Pen')  
        elif ans ==2:
            print('Pineapple') 
        elif ans == 3:
            print('Apple')
        else:
            print('Pineapple pen')
    except:
        break