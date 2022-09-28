from collections import deque
def solution(queue1, queue2):
    answer = 0
    total = sum(queue1) + sum(queue2)
    if sum(queue1) == sum(queue2):
        return 0
    if total % 2 != 0:
        return -1
    elif max(queue1) > total/2 or max(queue2) > total/2:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while sum(queue1) != sum(queue2):
        if sum(queue1) > sum(queue2):
            temp = queue1.popleft()
            queue2.append(temp)
            answer += 1
        elif sum(queue1) < sum(queue2):
            temp = queue2.popleft()
            queue1.append(temp)
            answer += 1
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))