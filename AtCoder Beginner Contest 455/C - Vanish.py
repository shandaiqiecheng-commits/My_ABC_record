from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
counts = Counter(a)
contributions = [val * count for val, count in counts.items()]
contributions.sort(reverse=True)
reduction = sum(contributions[:k])
print(total - reduction)