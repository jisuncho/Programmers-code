n = int(input())
temp = n
arr = [[" "]*n for i in range(n)]
x = 0
y = 0
flag = False
count = 0

while temp >= 3:
    if flag == False:
        for i in range(y, y + temp):
            arr[x][i] = "#"
        y = y + temp - 1

        for i in range(x,x + temp):
            arr[i][y] = "#"
        x = x + temp - 1

        for i in range(y, y-temp, -1):
            arr[x][i] = "#"
        y = y - temp + 1
        flag = True
        temp -= 2

    for i in range(x, x - temp, -1):
        arr[i][y] = "#"
    x = x - temp + 1
    count += 1
    if count == 2:
        temp -= 2
        count = 0
        if temp == 1:
            break

    for i in range(y, y + temp):
            arr[x][i] = "#"
    y = y + temp - 1
    count += 1
    if count == 2:
        temp -= 2
        count = 0
        if temp == 1:
            break

    for i in range(x,x + temp):
        arr[i][y] = "#"
    x = x + temp - 1
    count += 1
    if count == 2:
        temp -= 2
        count = 0
        if temp == 1:
            break

    for i in range(y, y-temp, -1):
        arr[x][i] = "#"
    y = y - temp + 1
    count += 1
    if count == 2:
        temp -= 2
        count = 0
        if temp == 1:
            break

for i in range(n):
    print(*arr[i])
   