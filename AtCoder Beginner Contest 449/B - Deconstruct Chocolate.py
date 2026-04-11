h, w, q = map(int, input().split())
for i in range (q):
    leixing, num = map(int, input().split())
    if leixing == 1:
        print(num * w)
        h -= num
    else:
        print(num * h)
        w -= num