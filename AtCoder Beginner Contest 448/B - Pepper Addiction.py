n, m = map(int,input().split())
lstc = list(map(int,input().split()))
demands = [0] * m
for i in range(1, n + 1):
    ai, bi = map(int,input().split())
    demands[ai - 1] += bi
ans = 0
for j in range(m):
    ans += min(demands[j], lstc[j])
print(ans)