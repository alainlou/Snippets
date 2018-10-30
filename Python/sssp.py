import sys
import heapq
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

edges = [[999999 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    x,y,w = [int(i) for i in input().split()]
    edges[x][y] = min(edges[x][y], w)

lengths = [-1] * n
visited = []
prev = 1
queue = [(edges[prev][i], i) for i in range(n+1) if edges[prev][i] < 999999]
heapq.heapify(queue)

while queue:
    curr = heapq.heappop(queue)
    for i in range(n):
        if(curr[0] + edges[curr[1]][i] < edges[prev][i]):
            edges[prev][i] = curr[0] + edges[curr[1]][i]
            edges[i][prev] = curr[0] + edges[curr[1]][i]
    prev = curr[1]
