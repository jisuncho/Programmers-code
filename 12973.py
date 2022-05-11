from collections import deque
def solution(s):
    answer = -1
    deq = deque()
    candy = ''
    for c in s:
        if len(deq) == 0:
            deq.append(c)
        else:
            candy = deq.pop()
            if candy == c:
                continue
            else:
                deq.append(candy)
                deq.append(c)
    if len(deq) == 0:
        return 1
    return 0