class Vertex:
    def __init__(self,data):
        self.data = data 
        self.visited = False
        self.group = 1 
        self.connections = []

# fails 4 testcases
def solve():
    n, m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    flag = False 
    for i in range(1,n+1):
        for j in graph[i].connections:
            if j <= i and graph[i].group == graph[j].group:
                flag = True
                break 
            if graph[i].group == graph[j].group:
                graph[j].group = 0 if graph[i].group else 1

    if flag:
        print("IMPOSSIBLE")
        return 

    for i in range(1,n+1):
        print(graph[i].group+1,end = " ")
    print()

if __name__ == '__main__':
    solve() 
