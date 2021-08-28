while True:
  try:
    n = int(input())
    s = int(input())
    l= list()
    r = list()
    for i in range(n):
        temp = list(map(int,input().split()))
        l.append(temp)
    x = ((n+1) // 2)-1
    y = ((n+1) // 2)-1
    w = s+1
    c = 0
    st = 1
    while True:
            for i in range(2):
              if w%4 == 1:#left
                for j in range(st):
                    r.append(l[x][y])
                    y -= 1
              elif w%4 == 2:#up
                for j in range(st):
                    r.append(l[x][y])
                    x -= 1
              elif w%4 == 3:#right
                for j in range(st):
                    r.append(l[x][y])
                    y += 1
              else:#down
                for j in range(st):
                    r.append(l[x][y])
                    x += 1
              w += 1
            st += 1
            if st == n:
                if w%4 == 1:#left
                  for j in range(st):
                      r.append(l[x][y])
                      y -= 1
                elif w%4 == 2:#up
                  for j in range(st):
                      r.append(l[x][y])
                      x -= 1
                elif w%4 == 3:#right
                  for j in range(st):
                      r.append(l[x][y])
                      y += 1
                else:#down
                  for j in range(st):
                      r.append(l[x][y])
                      x += 1
                break
    for i in range(n**2):
        if i == (n**2)-1:
            print(r[i])
        else:
            print(r[i],end='')
  except:
      break