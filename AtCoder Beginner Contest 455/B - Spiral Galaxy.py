h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
ans = 0
for h1 in range(h):
    for w1 in range(w):
        for h2 in range(h1, h):
            for w2 in range(w1, w):
                flag = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if grid[i][j] != grid[h1 + h2 - i][w1 + w2 - j]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    ans += 1
print(ans)