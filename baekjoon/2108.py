from collections import defaultdict
import sys

n = int(sys.stdin.readline().strip())
arrr = []
dic = defaultdict(int)
for i in range(n):
    a = int(sys.stdin.readline().strip())
    if dic[a]:
        dic[a] += 1
    else:
        dic[a] = 1
    arrr.append(a)


arrr = sorted(arrr)

def one(arrr):
    return round(sum(arrr)/n)

def two(arrr):
    return arrr[n//2]

def three(arrr):
    maxx = (0,0)
    same = []
    for i in dic:
        if dic[i] > maxx[1]:
            maxx = (i, dic[i])
            same = [i]
        elif dic[i] == maxx[1]:
            same.append(i)
    if len(same) > 1:
        return sorted(same)[1]
    else:
        return maxx[0]

def four(arrr):
    return arrr[-1] - arrr[0]

print(one(arrr))
print(two(arrr))
print(three(arrr))
print(four(arrr))