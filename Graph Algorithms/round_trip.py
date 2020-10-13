from collections import deque
class Vertex:
    def __init__(self,data):
        self.data = data 
        self.visited = False 
        self.parent = -1 
        self.connections = []
def printPath(graph,vertex):
    q = deque()
    q.append(vertex.data)
    while(vertex.parent != -1):
        vertex = graph[vertex.parent]
        q.appendleft(vertex.data)
    q.append(q[0])
    print(len(q))
    print(*q)

# todo (fails few test cases)
def bfs(graph,i):
    q = deque()
    q.append(i)
    count = 0
    while q:
        count += 1
        new = deque()
        for j in q:
            vertex = graph[j]
            if vertex.visited and count > 2: return vertex
            if vertex.visited: continue
            vertex.visited = True 
            for k in vertex.connections:
                if graph[k].visited: continue
                graph[k].parent = j
                new.append(k) 
        q = new

# fails 
def solve():
    n,m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    
    flag = None 
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[j].visited = False
            graph[j].parent = -1 
        flag = bfs(graph,i)
        if flag:
            break
    if not flag:
        print("IMPOSSIBLE")
        return 
    print(flag.data)
    printPath(graph,flag)
    for i in range(1,n+1):
        print(graph[i].data,graph[i].parent)

if __name__ == '__main__':
    solve()