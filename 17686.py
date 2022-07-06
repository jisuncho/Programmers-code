def solution(files):
    answer = []
    newfiles = []
    for file in files:
        flag = False
        numstart = 0
        numend = 0
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if flag == False and file[i].isdigit():
                numstart = i
                flag = True
            if flag == True and file[i].isdigit() != True:
                numend = i
                break
        if numend == 0:
            numend = len(file)
        head = file[:numstart]
        lowhead = head.lower()
        number = file[numstart:numend]
        tail = file[numend:]
        newfiles.append((head, lowhead, int(number), number, tail))
    
    newfiles = sorted(newfiles, key = lambda x : (x[1], x[2]))
    for head, lowhead, intnum, num, tail in newfiles:
        temp = ''
        temp += head+num+tail
        answer.append(temp)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))