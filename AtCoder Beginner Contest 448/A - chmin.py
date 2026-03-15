n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in a:
    if i < x :
        x = i
        print(1)
    else:
        print(0)