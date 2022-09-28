from copy import deepcopy
from collections import deque
def scorecount(score, info):
    ryan = 0
    apeach = 0
    for i in range(len(score)):
        if score[i] > info[i]:
            ryan += 10 - i
        elif score[i] <= info[i] and info[i] != 0:
            apeach += 10 - i
    if ryan <= apeach:
        return -1
    else:
        return ryan - apeach
    
def solution(n, info):
    answer = [-1]
    answerr = -1
    s= deque()
    s.append(([-1] * len(info), 0))
    
    while s:
        score, count = s.popleft()
        if count >= n:
            tempp = scorecount(score, info)
            if tempp >= answerr and tempp != -1:
                temp = []
                for i in score:
                    if i == -1:
                        temp.append(0)
                    else:
                        temp.append(i)
                answer = temp
                answerr = tempp
            continue
        for i in range(len(score)):
            if score[i] == -1:
                tscore = deepcopy(score)
                tscore[i] = 0
                s.append((tscore, count))
                if count + info[i] + 1 <= n:
                    score[i] = info[i] + 1
                    count += info[i] + 1
                    s.append((score,count))
                break
            if i == len(score)-1 and count < n:
                score[i] = score[i] + (n-count)
                s.append((score,count + (n-count)))
                
    return answer

print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))