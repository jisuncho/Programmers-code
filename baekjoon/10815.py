from collections import defaultdict
import sys

arr = []
dic = defaultdict(int)
n = int(sys.stdin.readline().strip())
temp = list(map(int,input().split()))
for i in range(len(temp)):
    dic[temp[i]] = 1
m = int(sys.stdin.readline().strip())
arr = list(map(int,input().split()))

for x in arr:
    if dic[x]:
        print(1)
    else:
        print(0)