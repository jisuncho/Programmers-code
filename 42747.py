def solution(citations):
    answer = 0
    cit = sorted(citations)
    
    for i in range(len(cit)):
        big = 0
        small = 0
        for c in cit:
            if i <= c:
                big += 1
            else:
                small += 1
        if big >= i and small <= i:
            answer = i
    return answer

print(solution([12, 11, 10, 9, 8, 1]))