def solve():
    mod = 10**9 + 7 
    dp = [ [0 for i in range(m+2)] for i in range(n+2) ]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1:
                if x[i-1] == 0 or x[i-1] == j:
                    dp[i][j] = 1 
            elif x[i-1] == 0 or x[i-1] == j:
                dp[i][j] = ((dp[i-1][j-1] + dp[i-1][j])%mod + dp[i-1][j+1])%mod 
    ans = 0 
    for i in range(1,m+1):
        ans = (ans + dp[n][i])%mod 

    print(ans)
        

if __name__ == '__main__':
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    solve()
    
