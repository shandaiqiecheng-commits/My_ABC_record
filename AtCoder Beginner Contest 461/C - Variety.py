import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())
from collections import defaultdict

color_groups = defaultdict(list)
for _ in range(n):
    c, v = map(int, input().split())
    color_groups[c].append(v)
A = []
B = []

for color, values in color_groups.items():
    values.sort(reverse=True)
    A.append(values[0])
    B.extend(values[1:])
A.sort(reverse=True)
B.sort(reverse=True)
sum_A = [0] * (len(A) + 1)
for i in range(len(A)):
    sum_A[i + 1] = sum_A[i] + A[i]
sum_B = [0] * (len(B) + 1)
for i in range(len(B)):
    sum_B[i + 1] = sum_B[i] + B[i]
max_total_value = -1
min_x = m
max_x = min(k, len(A))
for x in range(min_x, max_x + 1):
    rem = k - x
    if rem <= len(B):
        current_value = sum_A[x] + sum_B[rem]
        if current_value > max_total_value:
            max_total_value = current_value

print(max_total_value)
