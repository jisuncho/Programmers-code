def solution(phone_number):
    answer = ''
    temp = phone_number[-4:]
    for i in range(len(phone_number)-4):
        answer += "*"
        
    print(temp)
    return answer + temp