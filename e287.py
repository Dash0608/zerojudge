# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:10:44 2021

@author: 88690
"""
# 我幫你的各個變數加入註解，這樣有助於你debug、也有助於老師debug
# 縮排建議統一用tab鍵，按空白鍵不方便閱讀，不容易看出錯誤
# if x > 0:
#  if y > 0:
#   pass       -> 這樣就很難看誰對齊誰
# if x > 0:
#     if y > 0:
#         pass    -> 結構一目瞭然

s = list(map(int,input().split())) # s[0]: row, s[1]: column
l = list() # 地圖
st = 9999999999 # 地圖最小值
x = 0
y = 0
# sm = 0 沒用到所以刪掉
b = 1 # 是否加入此點至r
r = list() # 路徑
for i in range(s[0]):
    temp = list(map(int,input().split()))
    l.append(temp) # 儲存整張地圖進l
for i in range(s[0]):
    for j in range(s[1]):
        if st > l[i][j]:
            st = l[i][j]
            x = i#row 初始位置
            y = j#column 初始位置

r.append(l[x][y]) # 加入起點
l[x][y] = -1 # 起點走過了，見47行說明

# 我將你原本的 for t in range(0): 以後的部分改為我自己的邏輯
# 因為 range(0) for迴圈不會執行
while True:
    # z = 0 不需要了，我改成判斷l2是否是空的

    # 這裡我改成最下面再加入路徑，沒有加入代表結束、該印出來了
    '''
    if b:
        r.append(l[x][y]) # 判斷要不要加入路徑
    b = 0
    '''
    l2 = [] # 四周候選名單
    if x+1 < s[0] and l[x+1][y] >= 0: # 我加入了 >=0 條件，<0 代表走過了(等等會把走過的標-1)
        l2.append(l[x+1][y])
    if y+1 < s[1] and l[x][y+1] >= 0:
        l2.append(l[x][y+1])
    if y-1 >= 0 and l[x][y-1] >= 0:
        l2.append(l[x][y-1])
    if x-1 >= 0 and l[x-1][y] >= 0:
        l2.append(l[x-1][y])
    # 到此為止，l2只會有沒走過的、不超界的點。
    # 所以l2最小的一定可以走
    # 不過，要先判斷l2還有沒有東西，沒了代表要印出來了
    if len(l2) == 0:
        print(sum(r))
        break

    if x+1 < s[0] and l[x+1][y] == sorted(l2)[0]: # 找出最小的方向
        x_next = x + 1 # 這邊要小心，不能x = x + 1，會影響到下面的elif，x就變了！
        y_next = y
        r.append(l[x+1][y]) # 加入r
        l[x+1][y] = -1 # 走過了
    elif y+1 < s[1] and l[x][y+1] == sorted(l2)[0]: # 找出最小的方向
        x_next = x
        y_next = y + 1
        r.append(l[x][y+1])
        l[x][y+1] = -1
    elif y-1 >= 0 and l[x][y-1] == sorted(l2)[0]: # 找出最小的方向
        x_next = x
        y_next = y - 1
        r.append(l[x][y-1])
        l[x][y-1] = -1
    elif x-1 >= 0 and l[x-1][y] == sorted(l2)[0]: # 找出最小的方向
        x_next = x - 1
        y_next = y
        r.append(l[x-1][y])
        l[x-1][y] = -1
    else:
        pass

    x = x_next # 真的走
    y = y_next
'''
    for t in range(0):
        if x+1 < s[0]:
            if sorted(l2)[0] == l[x+1][y]:
                if not(l[x+1][y] in r):
                    z = 1
                    x = x + 1
                    b = 1        
                else:
                    b = 0
                    l2.remove(l2[0])
        if y+1 < s[1]: 
            if sorted(l2)[0] == l[x][y+1]:
                if not(l[x][y+1] in r):
                    z = 1
                    y = y + 1
                    b = 1 
                else:
                    b = 0
                    l2.remove(l2[0])
        if x-1 >= 0:
            if sorted(l2)[0] == l[x-1][y]:
                if not(l[x-1][y] in r):
                    z = 1
                    x = x - 1
                    b = 1
                else:
                    b = 0
                    l2.remove(l2[0])
        if y-1 >= 0:
            if sorted(l2)[0] == l[x][y-1]:
                if not(l[x][y-1] in r):
                    z = 1
                    y = y - 1
                    b = 1  
                else:
                    b = 0
                    l2.remove(l2[0])
    if z == 0:
        print(sum(r))
        break
'''