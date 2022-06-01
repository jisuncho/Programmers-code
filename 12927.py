from heapq import heapify, heappush, heappop
def solution(n, works):
    answer = 0
    heap = []
    
    for w in works:
        heappush(heap, (-w, w))
    
    while n>0:
        x, y = heappop(heap)
        if y == 0:
            return 0
        heappush(heap, (-(y-1), y-1))
        n -= 1
    
    for x, y in heap:
        answer += y*y
        
    return answer

print(solution(99, [2, 15, 22, 55, 55]))