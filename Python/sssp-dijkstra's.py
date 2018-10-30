import sys
import heapq

input = sys.stdin.readline

n,m = [int(i) for i in input().split()]
edges = []
start = 1
dist = [99999 for i in range(n+1)]
prev = [-1 for j in range(n+1)]

for _ in range(m):
    a,b,c = [int(i) for i in input().split()]
    heapq.heappush(edges,(c,a,b))
    heapq.heappush(edges,(c,b,a))

while(edges != set()):
    curr = heapq.heappop(edges)
    for i in range(n+1):
        
        
