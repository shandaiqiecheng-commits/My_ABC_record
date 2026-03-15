L, R, D, U = map(int, input().split())

ans = 0
# 遍历 x 坐标
for x in range(L, R + 1):
    abs_x = abs(x)
    # 对于固定的 x，我们需要统计在 [D, U] 范围内的 y，
    # 使得 max(abs_x, abs(y)) 是偶数。

    # 这种情况分为两部分：
    # 1. 如果 abs_x 本身是偶数：
    #    那么只要 abs(y) <= abs_x，max 就是 abs_x (偶数)，点就是黑色。
    #    如果 abs(y) > abs_x，则要求 abs(y) 是偶数。

    # 2. 如果 abs_x 是奇数：
    #    那么只有当 abs(y) > abs_x 且 abs(y) 是偶数时，max 才是偶数（黑色）。

    # 为了简化计算，直接判断每一行中符合条件的 y
    # 这种 O(N) 的做法在 2*10^6 范围内在 Python 中可能稍慢，但通常能过
    # 如果追求极致性能，可以使用数学分段统计 y 的个数

    # 判定函数：给定 x, y 返回是否为黑点
    # 这里直接逻辑拆解：
    if abs_x % 2 == 0:
        # 当 |y| <= abs_x 时，max 为 abs_x (偶数)，全是黑色
        # 当 |y| > abs_x 时，要求 |y| 为偶数

        # 拆分区间 [D, U]
        # 区间 A: [D, U] 中满足 |y| <= abs_x 的部分
        # 即 y 在 [max(D, -abs_x), min(U, abs_x)]
        y_low = max(D, -abs_x)
        y_high = min(U, abs_x)
        if y_low <= y_high:
            ans += (y_high - y_low + 1)

        # 区间 B: [D, U] 中满足 |y| > abs_x 且 |y| 是偶数的部分
        # y 在 [D, -abs_x - 1] 和 [abs_x + 1, U]
        for start, end in [(D, -abs_x - 1), (abs_x + 1, U)]:
            if start <= end:
                # 统计 [start, end] 之间 abs(y) 为偶数的个数
                # 等同于统计 y 为偶数的个数（因为偶数的绝对值还是偶数）
                # 统计 [start, end] 内偶数个数公式： (end//2) - ((start-1)//2) 仅限正数
                # 通用公式：
                count = (end // 2) - ((start - 1) // 2)
                ans += count
    else:
        # 当 abs_x 是奇数，要求 abs(y) > abs_x 且 abs(y) 是偶数
        for start, end in [(D, -abs_x - 1), (abs_x + 1, U)]:
            if start <= end:
                count = (end // 2) - ((start - 1) // 2)
                ans += count

print(ans)

