n = int(input())
l = list(map(int, input().split()))

# 这里的 memo 用来记录 (第几步, 当前坐标) 对应的最大穿过次数
memo = {}

def get_max_pass(idx, temp):
    # 终止条件：走完了所有步
    if idx == n:
        return 0
    
    # 检查是否已经计算过这个状态
    state = (idx, temp)
    if state in memo:
        return memo[state]
    
    # 你的思路：计算两个方向的新坐标
    left = temp - l[idx]
    right = temp + l[idx]
    
    # 计算选择左边能否穿过 0 (正负号改变即为穿过)
    pass_left = 1 if left * temp < 0 else 0
    res_left = pass_left + get_max_pass(idx + 1, left)
    
    # 计算选择右边能否穿过 0
    pass_right = 1 if right * temp < 0 else 0
    res_right = pass_right + get_max_pass(idx + 1, right)
    
    # 取两种选择中更好的那个
    memo[state] = max(res_left, res_right)
    return memo[state]

# 从第 0 步，初始位置 0.5 开始
print(get_max_pass(0, 0.5))

