a, b = map(int, input().strip().split(' '))
temp = ''
for j in range(b):
    for i in range(a):
        temp += "*"
    print(temp)
    temp = ''