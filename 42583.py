from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    s = deque()
    tw = deque(truck_weights)
    bw = 0
    
    while len(tw) > 0 or len(s) > 0:
        if len(s) != 0 and s[0][1] == time - bridge_length:
            a, b = s.popleft()
            bw -= a
        if len(tw) != 0 and (bw + tw[0]) <= weight:
            bw += tw[0]
            truck = tw.popleft()
            s.append((truck, time))
            
        time += 1
    return time