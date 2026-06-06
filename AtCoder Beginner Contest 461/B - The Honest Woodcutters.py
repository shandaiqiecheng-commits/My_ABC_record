n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = True
for i in range(n):
    if b[a[i] - 1] == i + 1:
        continue
    else:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")