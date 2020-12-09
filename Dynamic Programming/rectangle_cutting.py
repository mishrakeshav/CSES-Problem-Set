def solve():
    a,b = map(int,input().split())
    dp = [ [ 0 for i in range(b+1) ] for i in range(a+1) ]
    for i in range(a+1):
        for j in range(b+1):
            if(i==j):
                dp[i][j] = 0 
            else:
                ans  = float('inf')
                for k in range(1,i):
                    dp[i][j] = min(dp[i][j], dp[k][j] + dp[i-k][j] + 1)
                for k in range(1,j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j-k] + 1)
    print(dp[a][b])

if __name__ == '__main__':
    solve()