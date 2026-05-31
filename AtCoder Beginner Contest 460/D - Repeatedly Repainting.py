import sys
from collections import deque

def solve():
    # 优化输入读取
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    H = int(input_data[0])
    W = int(input_data[1])
    G = input_data[2:]
    
    # 检查特例情况：全白或全黑
    has_black = any('#' in row for row in G)
    has_white = any('.' in row for row in G)
    if not has_black or not has_white:
        for _ in range(H):
            print('.' * W)
        return

    # 使用边界防护垫（Padding），四周各加一圈
    W_padded = W + 2
    H_padded = H + 2
    
    # ==================== BFS 1: 计算到黑色格子的距离 d ====================
    # 初始全设为 0（边界默认为 0，代表已访问，BFS 不会越界到边界外）
    d = [0] * (H_padded * W_padded)
    q = deque()
    
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            idx = r * W_padded + c
            if G[r-1][c-1] == '#':
                d[idx] = 0
                q.append(idx)
            else:
                d[idx] = -1  # -1 代表未访问过
                
    # 8 个方向的一维偏移量
    offsets = [
        -W_padded - 1, -W_padded, -W_padded + 1,
        -1,                         1,
        W_padded - 1,  W_padded,  W_padded + 1
    ]
    
    while q:
        u = q.popleft()
        dist = d[u]
        next_dist = dist + 1
        for o in offsets:
            v = u + o
            if d[v] == -1:
                d[v] = next_dist
                q.append(v)

    # ==================== BFS 2: 计算到白色格子的距离 d_W ====================
    d_W = [0] * (H_padded * W_padded)
    q = deque()
    
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            idx = r * W_padded + c
            if G[r-1][c-1] == '.':
                d_W[idx] = 0
                q.append(idx)
            else:
                d_W[idx] = -1
                
    while q:
        u = q.popleft()
        dist = d_W[u]
        next_dist = dist + 1
        for o in offsets:
            v = u + o
            if d_v := d_W[v] == -1:
                d_W[v] = next_dist
                q.append(v)

    # ==================== 构造最终的网格输出 ====================
    ans = []
    for r in range(1, H + 1):
        row_chars = []
        for c in range(1, W + 1):
            idx = r * W_padded + c
            if G[r-1][c-1] == '.':
                # 初始为白：d 为偶数时最终为黑
                if d[idx] % 2 == 0:
                    row_chars.append('#')
                else:
                    row_chars.append('.')
            else:
                # 初始为黑：d_W 为奇数时最终为黑
                if d_W[idx] % 2 == 1:
                    row_chars.append('#')
                else:
                    row_chars.append('.')
        ans.append("".join(row_chars))
        
    print('\n'.join(ans))

if __name__ == '__main__':
    solve()