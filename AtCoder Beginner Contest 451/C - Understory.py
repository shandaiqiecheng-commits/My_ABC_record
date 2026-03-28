import heapq
Q = int(input())
treeh = []
lstq = [0] * Q
for i in range(Q):
    query, h = map(int,input().split())
    if query == 1:
        heapq.heappush(treeh,h)
    else:
        while treeh and treeh[0] <= h:
            heapq.heappop(treeh)
    lstq[i] = len(treeh)
for i in lstq:
    print(i)