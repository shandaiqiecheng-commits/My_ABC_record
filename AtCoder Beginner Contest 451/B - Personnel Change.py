n, m = map(int,input().split())
lst1 = [0] * n
lst2 = [0] * n
lst3 = [0] * m
for i in range(n):
    lst1[i], lst2[i] = map(int,input().split())
for i in lst1:
    lst3[i - 1] -= 1
for i in lst2:
    lst3[i - 1] += 1
for i in lst3:
    print(i)
