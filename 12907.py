def solution(n, money):
    rest = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                rest[i] += rest[i-m]
                
    return rest[n] % 1000000007
