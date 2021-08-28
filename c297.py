base = [0,0,0]
score = 0
out = 0
l = list()
for k in range(0,9):
    temp = list(map(str,input().split()))
    l.append(temp)
ot = int(input())
i = 0
while True:
    for j in range(0,9):
        if l[j][i+1] == '1B':
            if base[2] == 1:
                score += 1
                base[2] = 0
            if base[1] == 1:
                base[2] = 1
                base[1] = 0
            if base[0] == 1:
                base[1] = 1
                base[0] = 0
            if base[0] == 0:
                base[0] = 1
        if l[j][i+1] == '2B':
            if base[2] == 1:
                score += 1
                base[2] = 0
            if base[1] == 1:
                score += 1
                base[1] = 0
            if base[1] == 0:
                base[1] = 1
            if base[2] == 0 and base[0] == 1:
                base[2] = 1
                base[0] = 0
        if l[j][i+1] == '3B':
            if base[0] == 1:
                score += 1
                base[0] = 0
            if base[1] == 1:
                score += 1
                base[1] = 0
            if base[2] == 1:
                score += 1
                base[2] = 0
            if base[2] == 0:
                base[2] = 1
        if l[j][i+1] == 'HR':
            score += 1
            if base[0] == 1:
                score += 1
            if base[1] == 1:
                score += 1
            if base[2] == 1:
                score += 1
            base = [0,0,0]
        if l[j][i+1] == 'SO' or l[j][i+1] == 'FO' or l[j][i+1] == 'GO':
            out += 1
            if out%3 == 0 and out != 0:
                base = [0,0,0]
            if out >= ot:
                print(score)
                break
    i += 1
    if out >= ot:
        break