def solution(n, lost, reserve):
    answer = 0
    
    lost = set(lost)
    reserve = set(reserve)
    both = lost & reserve
    
    lost = lost - both
    reserve = reserve - both
    
    count = n
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                continue
            elif i + 1 in reserve:
                reserve.remove(i + 1)
            else:
                count -= 1
                
    return count