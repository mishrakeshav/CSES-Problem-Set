INF = float('inf')
MOD = 10**9 + 7 
#TODO

def solve():
    n,total = map(int,input().split())
    prices = list(map(int,input().split()))
    pages = list(map(int,input().split()))
    dp = [[0 for i in range(n)] for i in range(total + 1)]
    m = -INF 
    for i in range(1,total + 1):
        for j in range(n):
            if i - prices[j] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-prices[j]][j] + pages[j])
                m = max(dp[i][j],m)
    print('prices: ', prices)
    print('pages: ', pages)
    for i in range(total+1):
        print(i,'->',dp[i])
    print(m)    

def solve2():
    n,total = map(int,input().split())
    prices = list(map(int,input().split()))
    pages = list(map(int,input().split()))
    dp = [[0 for i in range(total + 1)] for i in range(n)]
    m = -INF 
    for i in range(n):
        for j in range(1,total + 1):
            if j - prices[i]:
                dp[i][i] = max(dp[i][j], dp[i][j - prices[i]] + pages[i])
                m = max(dp[i][j], m)
            
    print('prices: ', prices)
    print('pages: ', pages)
    for i in range(n):
        print(dp[i])
    print(m)    



if __name__ == '__main__':
    solve2()