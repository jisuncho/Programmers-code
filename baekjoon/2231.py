n = int(input())
answer = 0
for i in range(n):
    total = i
    for j in str(i):
        total += int(j)
    if total == n:
        answer = i
        break
print(answer)