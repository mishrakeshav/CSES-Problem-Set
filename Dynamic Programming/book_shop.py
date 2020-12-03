INF = float('inf')
MOD = 10**9 + 7 
#TODO


def solve():
    n,x =  map(int,input().split())
    prices = list(map(int,input().split()))
    pages = list(map(int,input().split()))
    dp = [ [0 for i in range(x+1)] for i in range(len(prices) + 1) ]
    for i in range(1,n+1):
        for j in range(1,x+1):
            dp[i][j] = dp[i-1][j]
            if j - prices[i-1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j - prices[i-1]] + pages[i-1])
    
    print(dp[n][x])




if __name__ == '__main__':
    solve()