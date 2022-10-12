import sys

wboard = ["WBWBWBWB", 
          "BWBWBWBW",
          "WBWBWBWB", 
          "BWBWBWBW",
          "WBWBWBWB", 
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW"]
bboard = ["BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",]
arr = []
minn = 10e9
n, m = map(int, input().split())
for i in range(n):
    arr.append(input())

def search(x, y):
    wcount = 0
    bcount = 0
    jtemp = 0
    itemp = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if arr[i][j] != wboard[itemp][jtemp]:
                wcount += 1
            if arr[i][j] != bboard[itemp][jtemp]:
                bcount += 1
            jtemp += 1
        itemp += 1
        jtemp = 0
    return min(wcount,bcount)

for i in range(0, n-7):
    for j in range(0, m-7):
 
        minn = min(minn, search(i, j))

print(minn)