n, m = map(int, input().split())
count = 1
while n % m != 0:
    m = n % m
    count += 1
print(count)