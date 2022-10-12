from collections import defaultdict

xdic = defaultdict(int)
ydic = defaultdict(int)
answer = ""
for i in range(3):
    x, y = input().split()
    if xdic[int(x)]:
        xdic[int(x)] += 1
    else:
        xdic[int(x)] = 1
    if ydic[int(y)]:
        ydic[int(y)] += 1
    else:
        ydic[int(y)] = 1

for i in xdic:
    if xdic[i] == 1:
        answer += str(i) + " "
for i in ydic:
    if ydic[i] == 1:
        answer += str(i)

print(answer)