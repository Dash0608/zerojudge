while True:        
    try:
        n = int(input())
        l = list()
        f = 0
        s = 0
        for i in range(n-1):
            l.append(list(map(int,input().split())))
        tree = [[l[0][0]],[l[0][1]]]
        for i in range(1,n-1):
             if l[i][1] in tree[0]:
                 tree.insert(0,[l[i][0]])
             elif l[i][0] in tree[len(tree)-1]:
                 tree.append([l[i][1]])  
             elif l[i][0] in tree[0]:
                 tree[tree.index(tree[0])+1].append(l[i][1])
             elif l[i][1] in tree[len(tree)-1]:
                 tree[tree.index(tree[0])].append(l[i][0])
        print(len(tree))
    except:
        break