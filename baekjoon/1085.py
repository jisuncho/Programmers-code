import sys

x, y, w, h = input().split()

left = int(x)
right = int(w) - int(x)
up = int(h) - int(y)
down = int(y)

answer = min(left,right,up,down)

print(answer)