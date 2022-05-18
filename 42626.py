from heapq import heappop, heapify, heappush
def solution(sc, K):
    answer = 0
    heapify(sc)
    
    while len(sc) > 1:
        a = heappop(sc)
        if a >= K:
            return answer
        b = heappop(sc)
        heappush(sc, a+(b*2))
        answer += 1
    return -1


