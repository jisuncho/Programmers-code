from collections import deque
n, k = map(int, input().split())
arr = deque(map(int, input().split()))
count = 1
for i in range(k):
	arr.popleft()
while arr:
	count += 1
	for i in range(k-1):
		if arr:
			arr.popleft()
		else:
			break
print(count)