def solution(n, times):
    answer = 0
    times = sorted(times)
    left = 1
    right = n * times[-1]
    
    
    while(left <= right):
        total = 0
        mid = (left + right) // 2
        for time in times:
            total += mid // time
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(solution(6, [7,10]))