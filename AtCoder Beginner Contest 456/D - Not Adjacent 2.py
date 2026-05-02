s = input()
MOD = 998244353
dp = {'a': 0, 'b': 0, 'c': 0}
    
for char in s:
    if char == 'a':
        new_additions = (dp['b'] + dp['c'] + 1) % MOD
        dp['a'] = (dp['a'] + new_additions) % MOD
    elif char == 'b':
        new_additions = (dp['a'] + dp['c'] + 1) % MOD
        dp['b'] = (dp['b'] + new_additions) % MOD
    elif char == 'c':
        new_additions = (dp['a'] + dp['b'] + 1) % MOD
        dp['c'] = (dp['c'] + new_additions) % MOD

ans = (dp['a'] + dp['b'] + dp['c']) % MOD
print(ans)
