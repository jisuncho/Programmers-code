from heapq import heapify, heappush, heappop
def solution(jobs):
    answer = 0
    joblen = len(jobs)
    jobs = sorted(jobs, key = lambda x:x[0])
    visited = [False] * len(jobs)
    heap = []
    time = 0
    
    while joblen != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= time and visited[i] == False:
                heappush(heap, (jobs[i][1], jobs[i][0]))
                visited[i] = True
        
        if heap:
            taketime, starttime = heappop(heap)
            time += taketime
            answer += time - starttime
            joblen -= 1
        else:
            time += 1

    return answer//len(jobs)