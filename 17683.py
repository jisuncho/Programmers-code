def music_changer(music):
    nmusic = ''
    flag = False
    for i in range(len(music)-1):
        if flag == True:
            flag = False
            continue
        if music[i+1] == '#':
            nmusic += music[i].lower()
            flag = True
        else:
            nmusic += music[i]
    if music[-1] != '#':
        nmusic += music[-1]
    return nmusic

def solution(m, musicinfos):
    answer = '(None)'
    long = 0
    lenm = len(m)
    m = music_changer(m)
    for musics in musicinfos:
        time = 0
        akpo = ''
        start, end, name, music = musics.split(',')
        music = music_changer(music)
        time += (int(end[0:2]) - int(start[0:2])) * 60
        time += (int(end[3:5]) - int(start[3:5]))
        for i in range(time):
            akpo += music[i%len(music)]
        if m in akpo:
            if answer == '(None)':
                answer = name
                long = time
            else:
                if time > long:
                    answer = name
                    long = time
    return answer
    
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))