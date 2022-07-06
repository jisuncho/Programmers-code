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

print(music_changer('CC#BCC#BCC#BCC#B'))