arr = []

while(True):
    a, b ,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    arr.append((a,b,c))

for a, b, c in arr:
    maxx = max(a,b,c)
    if ((a*a + b*b + c*c) / 2) ==  (maxx * maxx):
        print("right")
    else:
        print("wrong")