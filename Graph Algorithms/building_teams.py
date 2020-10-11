class Vertex:
    def __init__(self,data):
        self.data = data 
        self.visited = False
        self.group = 1 
        self.connections = []



# first we have to see if there is a cycle in the undirected graph (todo) 
# then we can assign groups to each vertex (done)
def solve():
    n, m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    s = set()
    flag = False
    for i in range(1,n+1):
        s.add(i)
        for j in graph[i].connections:
            if j in s and graph[i].group == graph[j].group:
                flag = True 
                break
            if graph[i].group == graph[j].group:
                graph[j].group = 0 if graph[i].group else 1 
    if flag:
        print("IMPOSSIBLE")
    else:
        for i in range(1,n+1):
            print(graph[i].group + 1, end = " ")
        print() 
    
if __name__ == '__main__':
    solve() 