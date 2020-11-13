
INF = float('inf')
MOD = 10**9 + 7

def solve():
    n = int(input()) 
    grid = []
    dp = []
    for _ in range(n):
        col = input()
        grid.append(col)
        dp.append([0]*(n))
    
    dp[-1][-1] = 1
    if grid[-1][-1] == '*' or dp[0][0] == '*':
        print(0)
        return
    for i in range(n-2,-1,-1):
        if grid[-1][i] != '*':
            dp[-1][i] += dp[-1][i+1]
        if grid[i][-1] != '*':
            dp[i][-1] = dp[i+1][-1]
    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            if grid[i][j] != '*':
                dp[i][j] += dp[i][j+1] + dp[i+1][j]
                dp[i][j] %= MOD

    print(dp[0][0]) 
    
    
if __name__ == '__main__':
    solve()