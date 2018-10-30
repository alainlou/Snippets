import sys

input = sys.stdin.readline

c,r,d = [int(i) for i in input().split()]

tree = {i:set() for i in range(1,c+1)}

dest = set()

visited = set()

for i in range(r):
    x,y,w = [int(i) for i in input().split()]
    tree[x].add((y,w))
    tree[y].add((x,w))

for i in range(d):
    dest.add(int(input()))

maximum = 1000000
#Minimum spanning tree with Prim's
stack = [(1,1000000)]
while True:
    if dest-visited == set():
        print(maximum)
        break
    vertex = stack.pop(stack.index(max(stack, key=lambda x:x[1])))
    if vertex[0] not in visited:
        if vertex[1] < maximum:
            maximum = vertex[1]
        visited.add(vertex[0])
        stack.extend([i for i in tree[vertex[0]] if i[0] not in visited])
