import sys

def devil(n):
    count = 0
    for i in str(n):
        if i == "6":
            count += 1
        else:
            count = 0
        if count >= 3:
            return True
    return False

n = int(sys.stdin.readline().strip())
count = 0
i = 665
while(True):
    i += 1
    if devil(i):
        count += 1
    if count == n:
        print(i)
        break
