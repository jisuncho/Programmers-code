from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
        
    print(win)
    print(lose)
    for i in range(1, n+1):
        for loser in win[i]:
            lose[loser].update(lose[i])
        for winner in lose[i]:
            win[winner].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))