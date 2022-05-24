from collections import deque
def alright(p):
    r = 0
    l = 0
    for i in range(len(p)):
        if p[0] == ')':
            return False
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if r > l:
            return False
    return True
def solution(p):
    answer = ''
    u = []
    v = []
    s = deque(p)
    flag = True
    left = 0
    right = 0
    if not p:
        return []

    while s:
        x = s.popleft()

        if right == left and flag == False:
            v.append(x)
            continue

        if flag == True:
            flag = False
            u.append(x)
            if x == ')':
                right += 1
            else:
                left += 1
        else:
            if x == ')':
                    right += 1
                    u.append(x)
            else:
                left += 1
                u.append(x)

    if alright(u):
        print(u,v)
        return ''.join(u) + ''.join(solution(v))
    else:
        answer += '('
        answer += ''.join(solution(v))
        answer += ')'
        for i in range(1,len(u)-1):
            if u[i] == "(":
                answer += ')'
            else:
                answer += '('

    return answer

print(solution("(()())()"))