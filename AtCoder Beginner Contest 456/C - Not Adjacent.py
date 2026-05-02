s = input()
n = len(s)
MOD = 998244353
total_count = 0
current_length = 1
    
for i in range(1, n):
    if s[i] != s[i-1]:
        current_length += 1
    else:
        total_count += (current_length * (current_length + 1)) // 2
        total_count %= MOD
        current_length = 1

total_count += (current_length * (current_length + 1)) // 2
total_count %= MOD
    
print(total_count)
