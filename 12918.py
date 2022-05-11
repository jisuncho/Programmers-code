def solution(s):
    answer = True
    num = ['1','2','3','4','5','6','7','8','9','0']
    if len(s) not in [4,6]:
        return False
    
    for c in s:
        if c not in num:
            answer = False
    
    return answer