import sys
from collections import defaultdict
dic = defaultdict(int)
n = int(sys.stdin.readline().strip())
narr = list(map(int, (input().split())))
m = int(sys.stdin.readline().strip())
marr = list(map(int, (input().split())))
answer = ""
for x in narr:
    if dic[x]:
        dic[x] += 1
    else:
        dic[x] = 1

for x in marr:
    if dic[x]:
        answer += str(dic[x]) + " "
    else:
        answer += "0 "

print(answer)