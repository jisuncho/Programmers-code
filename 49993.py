def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        num = 0
        flag = False
        for i in range(len(st)):
            if st[i] in skill:
                if st[i] == skill[num]:
                    num += 1
                else:
                    flag = True
        if flag == False:
            answer += 1
    return answer