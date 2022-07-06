def solution(record):
    answer = []
    userlist = dict()
    for rec in record:
        print(rec)
        move, uid, name = rec.split()
        print(move, uid, name)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))