from itertools import permutations
def solution(numbers):
    answer = ''
    maxx = 0
    num = permutations(numbers, len(numbers))
    for n in num:
        temp = ''
        for i in range(len(n)):
            temp += str(n[i])
        maxx = max(int(temp),maxx)
    answer = str(maxx)
    print(answer)
    return answer

solution([6, 10, 2])