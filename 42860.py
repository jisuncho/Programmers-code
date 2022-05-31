from copy import deepcopy
import sys
from collections import deque
def solution(name):
    s = deque()
    move = 0
    answer = sys.maxsize
    dicc = {
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1
    }
    
    comp = [False] * len(name)
    compcount = 0
    curr = 0
    for i in range(len(name)):
        if name[i] == 'A':
            comp[i] = True
            compcount += 1
            
    if not comp[curr]:
        move += dicc[name[curr]]
        compcount += 1
        comp[curr] = True
    
    s.append((comp, compcount, move, curr))
    
    while s:
        c, cc, m, cr = s.popleft()
        if cc == len(name):
            answer = min(m,answer)
            continue
        
        r = 0
        l = 0
        
        temp_c = deepcopy(c)
        temp_cc = cc
        temp_m = m
        temp_cr = cr
        
        for i in range(1,len(name)+1):
            if not c[(cr+i)%len(name)]:
                r = i
                temp_m += dicc[name[(cr+r)%len(name)]]
                temp_m += r
                temp_cc += 1
                temp_cr = (cr+r)%len(name)
                temp_c[temp_cr] = True
                s.append((temp_c, temp_cc, temp_m, temp_cr))
                break
        
        temp_c = deepcopy(c)
        temp_cc = cc
        temp_m = m
        temp_cr = cr
        
        for i in range(1,len(name)+1):
            if not c[(cr-i)%len(name)]:
                l = i
                temp_m += dicc[name[(cr-l)%len(name)]]
                temp_m += l
                temp_cc += 1
                temp_cr = (cr-l)%len(name)
                temp_c[temp_cr] = True
                s.append((temp_c, temp_cc, temp_m, temp_cr))
                break
        
    return answer