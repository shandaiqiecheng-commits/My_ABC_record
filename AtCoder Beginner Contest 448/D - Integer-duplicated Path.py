import sys

# 必须增加递归深度
sys.setrecursionlimit(300000)

n = int(input())
a = list(map(int, input().split()))

# 建立邻接表
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
results = [""] * (n + 1)
# path_set 记录当前路径上的数字出现的次数
path_set = {}


def dfs(u, p, has_duplicate):
    val = a[u - 1]

    # 检查当前节点的值是否引起了新的重复
    current_duplicate = has_duplicate
    if val in path_set and path_set[val] > 0:
        current_duplicate = True

    # 记录答案
    results[u] = "Yes" if current_duplicate else "No"

    # 将当前值加入路径记录
    path_set[val] = path_set.get(val, 0) + 1

    # 递归子节点
    for v in adj[u]:
        if v != p:
            dfs(v, u, current_duplicate)

    # 回溯：离开该节点时，将其从路径记录中减去
    path_set[val] -= 1


# 从节点 1 开始，父节点设为 -1，初始重复状态为 False
dfs(1, -1, False)

# 按顺序输出结果
for i in range(1, n + 1):
    print(results[i])
