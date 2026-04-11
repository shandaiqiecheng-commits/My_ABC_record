# 处理输入部分
n = int(input())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
m = int(input())
s = []
for _ in range(m):
    si = input()
    s.append(si)

# 按长度对字符串进行分组
from collections import defaultdict
dict_s = defaultdict(set) # 当你访问一个不存在的键（Key）时，它不会报错，而是会自动为你创建一个空的 set（集合）
for si in s:
    dict_s[len(si)].add(si)
# 列出脊椎每一位 i 所允许的字符集
dict_c = defaultdict(set)
for i in range(n):
    for j in dict_s[a[i]]:
        dict_c[i].add(j[b[i] - 1])
# 对每一个单词进行判断        
for si in s:
    # 条件1：脊椎字符串长度必须等于 N
    if len(si) != n:
        print("No")
        continue
    # 条件2：脊椎的每一位字母是否都在dict_c中
    flag = True
    for i in range(n):
        if si[i] not in dict_c[i]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
