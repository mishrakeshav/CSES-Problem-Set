from collections import deque
class Vertex:
    def __init__(self,data):
        self.data = None 
        self.visited = False
        self.connections = list()

def dfs(graph,i):
    queue = deque()
    queue.appendleft(i)
    while(len(queue)):
        v = graph[queue.pop()]
        v.visited = True 
        for i in v.connections:
            if graph[i].visited: continue
            queue.append(i)
    
def solve():
    n, m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    
    nodes = []
    for i in range(1,n+1):
        if graph[i].visited: continue
        nodes.append(i)
        dfs(graph,i)
    
    print(len(nodes)-1)
    for i in range(1,len(nodes)):
        print(nodes[i-1],nodes[i])

if __name__ == '__main__':
    solve()