from collections import deque

def solution(numbers, target):
    answer = 0
    s = deque()
    
    s.append((numbers[0],1))
    s.append((-numbers[0],1))
    
    while s:
        a,b = s.pop()
        for x in [numbers[b],-numbers[b]]:
            na = a + x
            nb = b + 1
            if nb == len(numbers):
                if na == target:
                    answer += 1
            else:
                s.append((na,nb))
    
    return answer

print(solution([4, 1, 2, 1], 4))