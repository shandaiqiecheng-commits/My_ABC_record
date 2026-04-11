t, x = map(int,input().split())
a = list(map(int,input().split()))
print(0, a[0])
temp = a[0]
for i in range(1, t + 1):
    if abs(a[i] - temp) >= x:
        temp = a[i]
        print(i, a[i])