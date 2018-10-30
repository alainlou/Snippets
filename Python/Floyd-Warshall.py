import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]

edges = [[99999 for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
    edges[i][i] = 0

for _ in range(m):
    a,b,c = [int(i) for i in input().split()]
    edges[a][b] = min(edges[a][b], c)
    edges[b][a] = min(edges[b][a], c)

for i in range(len(edges)):
    for j in range(len(edges)):
        for k in range(len(edges)):
            if (edges[i][j] + edges[j][k]) < edges[i][k]:
                edges[i][k] = edges[i][j] + edges[j][k]
                edges[k][i] = edges[i][j] + edges[j][k]
                
for i in range(1, n+1):
    if(edges[1][i] != 99999):
        print(edges[1][i])
    else:
        print(-1)
