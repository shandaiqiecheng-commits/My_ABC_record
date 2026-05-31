n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
count = 0
a_idx = 0
b_idx = 0
while a_idx < n and b_idx < m:
    if B[b_idx] > 2 * A[a_idx]:
        b_idx += 1
    else:
        count += 1
        a_idx += 1
        b_idx += 1
print(count)