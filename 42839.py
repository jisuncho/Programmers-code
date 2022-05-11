from itertools import permutations
from math import sqrt

def primenumber(x):
    for i in range (2, int(sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True
                    
def solution(numbers):
    answer = 0
    answers = []
    for i in range(1, len(numbers)+1):
        comb = permutations(numbers, i)
        for com in comb:
            temp = ''
            for num in com:
                temp += num
            if primenumber(int(temp)) and int(temp) not in [0,1]:
                print(int(temp))
                if int(temp) not in answers:
                    answer += 1
                    answers.append(int(temp))
    return answer