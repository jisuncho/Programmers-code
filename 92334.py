from collections import defaultdict
def solution(id_list, reports, k):
    answer = []
    arr = defaultdict(int)
    mail = defaultdict(int)
    dic = defaultdict(set)

    for report in reports:
        a,b = report.split()
        dic[a].add(b)
    
    print(dic)
    for x in dic.keys():
        for y in dic[x]:
            if arr[y]:
                arr[y] += 1
            else:
                arr[y] = 1
    print(arr)
    
    for x in arr.keys():
        if arr[x] >= 2:
            for a in dic.keys():
                if x in dic[a]:
                    if mail[a]:
                        mail[a] += 1
                    else:
                        mail[a] = 1

    for id in id_list:
        answer.append(mail[id])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))