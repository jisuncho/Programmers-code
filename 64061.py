from collections import deque
def solution(board, moves):
    answer = 0
    s = deque()
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if s and s[0] == board[i][move-1]:
                    s.popleft()
                    answer += 2
                    break
                else:
                    s.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))