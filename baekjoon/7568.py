import sys

n = int(sys.stdin.readline().strip())
arr = []
answer = []
answerstr = ""
for x in range(n):
    arr.append((input().split()))

for x, y in arr:
    count = 1

    for dx, dy in arr:
        if int(x) < int(dx) and int(y) < int(dy):
            count += 1
    answer.append(count)

for x in answer:
    answerstr += str(x)+ " "
print(answerstr)