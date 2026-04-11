m, d = map(int, input().split())
if m == d:
    if m == 3 or m == 5 or m == 7 or m == 9:
        print("Yes")
    else:
        print("No")
elif m == 1 and d == 7:
    print("Yes")
else:
    print("No") 