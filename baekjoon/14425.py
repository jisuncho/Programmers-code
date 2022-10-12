import sys
narr = []
marr = []
answer = 0
n, m = input().split()
for i in range(int(n)):
    narr.append(str(sys.stdin.readline().strip()))
for i in range(int(m)):
    marr.append(str(sys.stdin.readline().strip()))

for x in marr:
    if x in narr:
        answer += 1

print(answer)