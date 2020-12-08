def solve():
    n = int(input())
    mx = n*1000
    x = list(map(int,input().split()))
    dp = [ [ False for i in range(mx+1) ] for i in range(n+1) ]
    dp[0][0] = True 
    for i in range(1,n+1):
        for j in range(mx+1):
            dp[i][j] = dp[i-1][j]
            if j - x[i-1] >= 0:
                dp[i][j] = dp[i][j] or dp[i-1][j-x[i-1]]
    
    possible = []
    for i in range(1,mx+1):
        if dp[n][i]:
            possible.append(i)
    print(len(possible))
    print(*possible)
if __name__ == '__main__':
    solve()