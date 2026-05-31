import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (r1 + r2) ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2 >= abs(r1 - r2) ** 2:
        print("Yes")
    else:
        print("No")
