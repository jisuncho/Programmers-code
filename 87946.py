from collections import deque
import copy
def solution(k, dungeons):
    answer = -1
    s = deque()
    for i in range(len(dungeons)):
        temp = [False] * len(dungeons)
        if dungeons[i][0] <= k:
            temp[i] = True
            s.append((temp, k - dungeons[i][1], 1))
            
    while s:
        visited, nk, count = s.pop()
        flag = False
        for i in range(len(dungeons)):
            temp = copy.deepcopy(visited)
            if visited[i] == False and dungeons[i][0] <= nk:
                flag = True
                temp[i] = True
                s.append((temp, nk - dungeons[i][1], count + 1))
        if flag == False:
            answer = max(answer, count)
    return answer
print(solution(80,[[80,20],[50,40],[30,10]]	))