
class Vertex:
    def __init__(self,data):
        self.data = data 
        self.visited = False 
        self.connections = []

def solve():
    n,m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    
    # check if there is a cycle and if there is a cycle 
    # then print one of the paths 
    # todo 
    
if __name__ == '__main__':
    solve()