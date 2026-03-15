n, l, r = map(int, input().split())
s = list(input())
ans = 0
cnt = [0] * 26

    # 初始窗口范围：[j-R, j-L]
    # 我们遍历 j，同时维护 i_left 和 i_right 指针
    # 实际上，当 j 增加 1 时：
    # 新进入窗口的元素是 s[j-L]
    # 离开窗口的元素是 s[j-R-1]

for j in range(n):
    # 1. 将新进入窗口右边界的字符加入计数
    # 窗口右侧索引是 j - l
    right_idx = j - l
    if right_idx >= 0:
        char_code = ord(s[right_idx]) - ord('a')
        cnt[char_code] += 1

    # 2. 将滑出窗口左边界的字符移除计数
    # 窗口左侧索引的前一个位置是 j - r - 1
    left_out_idx = j - r - 1
    if left_out_idx >= 0:
        char_code = ord(s[left_out_idx]) - ord('a')
        cnt[char_code] -= 1

    # 3. 累加当前字符 s[j] 在窗口内出现的次数
    if j >= l:
        current_char_code = ord(s[j]) - ord('a')
        ans += cnt[current_char_code]

print(ans)

