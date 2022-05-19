from collections import deque
def solution(progresses, speeds):
    answer = []
    count = 0
    answercount = 0
    s = deque()
    for i in range(len(progresses)):
        s.append((progresses[i],speeds[i]))
    flag = True
    while s:
        a, b = s.popleft()
        if count * b >= 100 - a:
            answercount += 1
            continue
        if (100 - a) % b == 0:
            if flag == True:
                flag = False
            else:
                answer.append(answercount)
                answercount = 0
            count = (100 - a) // b
            answercount += 1

        else:
            if flag == True:
                flag = False
            else:
                answer.append(answercount)
                answercount = 0
            count = ((100 - a) // b) + 1
            answercount += 1
            
    answer.append(answercount)
    
    return answer


print(solution(	[5, 5, 5], [21, 25, 20]))