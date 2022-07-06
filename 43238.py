def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer

print(solution(6, [7,10]))