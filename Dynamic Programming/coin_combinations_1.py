def solve():
    MOD = 10**9 + 7
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))
    coins.sort()
    dp = [0]*(x+1)
    dp[0] = 1
    for i in range(x+1):
        for j in coins:
            if i - j >= 0:
                dp[i] = (dp[i]%MOD + dp[i-j]%MOD)%MOD
            else:
                break
    print(dp[x]) 

if __name__ == '__main__':
    solve()