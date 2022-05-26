from collections import deque
def solution(priorities, location):
    answer = 0
    pp = sorted(priorities)
    s = deque()
    
    for i in range(len(priorities)):
        s.append((priorities[i],i))
                   
    while True:
        p, l = s.popleft()
        if p == pp[-1]:
            pp.pop()
            answer += 1
            if l == location:
                return answer
        else:
            s.append((p,l))

print(solution([2, 1, 3, 2],	2))