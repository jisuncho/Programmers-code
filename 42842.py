def solution(brown, yellow):
    answer = []
    add = brown + yellow
    tup = []
    for i in range(1,add//2):
        if add % i == 0:
            tup.append((i,add/i))
    
    for i, j in tup:
        if 2*i + 2*j - 4 == brown:
            if i < j:
                answer.append(j)
                answer.append(i)
            else:
                answer.append(i)
                answer.append(j)
            break
    return answer