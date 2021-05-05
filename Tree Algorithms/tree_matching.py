n = int(input())

nodes = dict()
for i in range(1,n+1):
    nodes[i] = []

for i in range(n-1):
    a,b = map(int,input().split())
    nodes[a].append(b)


