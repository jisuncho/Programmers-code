import sys

k = int(sys.stdin.readline().strip())
arr = []
xmax = 0
ymax = 0
save1 = 0
save2 = 0
for i in range(6):
    a, b = map(int, input().split())
    if a in [1,2]:
        xmax = max(xmax, b)
    else:
        ymax = max(ymax, b)
    arr.append((a,b))

arr = arr + arr + arr
real = []
flag = False
for i in range(len(arr)):
    if flag == False and (arr[i][1] == xmax or arr[i][1] == ymax):
        flag = True
        continue
    if flag == True and (arr[i][1] == xmax or arr[i][1] == ymax):
        real = arr[i-1:i+7]
        break
    else:
        flag = False

print(real)
flagx = False
flagy = False
count = 2
for a, b in real:
    if b == xmax and flagy == False:
        flagx = True
        count -= 1
        continue
    if flagx == False and b == ymax:
        flagy = True
        count -= 1
        continue
    if count == 1:
        count = 0
        continue
    if count == 0:
        if flagx == True:
            save1 = xmax - b
            count = -1
            continue
        if flagy == True:
            save1 = ymax - b
            count = -1
            continue
    if count == -1:
        if flagx == True:
            save2 = b
            print((xmax * ymax - save1*save2)* k)
            break
        if flagy == True:
            save2 = b
            print((xmax * ymax - save1*save2) * k)
            break