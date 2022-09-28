from collections import defaultdict, deque
def solution(n, wires):
    answer = 10e9
    dic = defaultdict(set)
    for a, b in wires:
        dic[a].add(b)
        dic[b].add(a)
    
    for a, b in wires:
        one = deque()
        one.append(a)
        visited = [False] * (n + 1)
        visited[a] = True
        count = 1

        while one:
            curr = one.popleft()
            for x in dic[curr]:
                if visited[x] == False and x != b:
                    one.append(x)
                    visited[x] = True
                    count += 1
        
        answer = min(answer, abs(n - count - count))
        
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))