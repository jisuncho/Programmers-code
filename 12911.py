def solution(n):
    answer = 0
    onecount = 0
    nn = bin(n)
    for i in range(2,len(nn)):
        if nn[i] == '1':
            onecount += 1
    
    print(onecount)
    while True:
        n += 1
        count = 0
        for i in range(2,len(bin(n))):
            if bin(n)[i] == '1':
                count += 1
        if count == onecount:
            return n
    
    return answer