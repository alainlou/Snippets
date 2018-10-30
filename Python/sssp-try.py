import heapq

n,m = [int(i) for i in input().split()]

edges = {k:set() for k in range(n)}

for i in range(m):
    a,b,c = [int(i) for i in input().split()]
    edges[a].add([c,b])
    edges[b].add([c,a])

pq = heapq
