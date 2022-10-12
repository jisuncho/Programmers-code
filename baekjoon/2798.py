import sys
from itertools import combinations

n, m = input().split()
arr = list(map(int, input().split()))
temp = combinations(arr, 3)
maxx = 0
for x in temp:
    t = sum(list(x))
    if t <= int(m):
        maxx = max(maxx, t)

print(maxx)
