l = list()
while True:
    try:
        t = int(input())
        l.append(t)
        l.sort()
        if len(l)%2==0:
            print((l[len(l)//2]+l[(len(l)//2)-1])//2)
        else:
            print(l[(len(l)//2)])
    except:
        break