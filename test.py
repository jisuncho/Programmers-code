# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
arr = []
for i in range(user_input-1, 0, -1):
	temp = user_input // i
	if temp not in arr:
		arr.append(temp)
print(len(arr))
