h, w = map(int, input().split())
lst = [ ["."] * w ] * h 
lst[0] = ["#"] * w
lst[h - 1] = ["#"] * w
for i in range(1, h):
    lst[i][0] = "#"
    lst[i][w - 1] = "#"
for i in lst:
    for j in i:
        print(j, end = "")
    print("")
    
