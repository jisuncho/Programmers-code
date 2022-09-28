import math
def primenumber(x):
    if x == 1:
        return False
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    return True			# 전부 나눠떨어지지 않으면 True
def solution(n, k):
    answer = 0
    x = 1
    num = []
    while(k ** x < n):
        x += 1

    for i in range(x-1 , 0, -1):
        if n // (k ** i) >= 1:
            num.append(n // (k ** i))
            n = n % (k ** i)
        else:
            num.append(0)
    num.append(n)

    temp = ""
    for i in num:
        if i != 0:
            temp += str(i)
        else:
            if temp != "" and primenumber(int(temp)):
                answer += 1
                temp = ''
            else:
                temp = ''
    if temp != "" and primenumber(int(temp)):
        answer += 1
    return answer

print(solution(437674,3))