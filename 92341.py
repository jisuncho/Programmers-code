from collections import defaultdict
def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    fee = [0] * 9999
    
    for record in records:
        time, num, status = record.split()
        if status == "IN":
            dic[num].append(time)
        else:
            xh, xm = dic[num][-1].split(":")
            yh, ym = time.split(":")
            dic[num].pop()
            zh = int(yh) - int(xh)
            zm = int(ym) - int(xm)
            temp = (zh * 60) + zm
            fee[int(num)] += temp
    
    
    for d in dic:
        if dic[d]:
            xh, xm = dic[d][-1].split(":")
            temp = ((23-int(xh)) * 60) + (59-int(xm))
            fee[int(d)] += temp
      
    for f in fee:
        if f != 0:
            if f <= fees[0]:
                answer.append(fees[1])
            else:
                if (f-fees[0]) % fees[2] == 0:
                    answer.append(fees[1] + (((f-fees[0])//fees[2]) * fees[3]))
                else:
                    answer.append(fees[1] + (((f-fees[0])//fees[2]+ 1) * fees[3]))
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))