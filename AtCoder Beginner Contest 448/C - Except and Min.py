n, q = map(int,input().split())
lst_a = list(map(int,input().split()))
balls = []
for i in range(n):
    balls.append((lst_a[i], i + 1))
balls.sort()
top_6 = balls[:6]
for _ in range(q):
    k = int(input())
    query = list(map(int,input().split()))
    for a, idx in top_6:
        if idx not in query:
            print(a)
            break