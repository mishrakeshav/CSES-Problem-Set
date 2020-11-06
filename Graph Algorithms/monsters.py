def dfs(i,j, level,n,m):
    global matrix, info, vector1, vector2,
    info[i][j][level] = 1 
    for k in range(4):
        y = i + vector1[k]
        x = j + vector2[k]
        if 0 <= y < n and  0 <= x < m and matrix[y][x] == ".":
            dfs(y,x,level + 1,n,m)

def solve():
    global matrix, info, vector1, vector2
    n,m = map(int,input().split())
    for _ in range(n):
        matrix.append(list(input()))
    info = []
    for _ in range(n):
        l = []
        for __ in range(m):
            l.append(dict())
        info.append(l)
    a,b = None,None 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "M":
                bfs(i,j,0,n,m)
            elif matrix[i][j] == "A":
                a,b = i, j
    
    for i in info:
        print(i)
        
    
    
    


    
    
    
    
if __name__ == '__main__':
    matrix = []
    info = []
    vector1 = [0, -1, 1, 0]
    vector2 = [-1, 0, 0, 1]
    solve()