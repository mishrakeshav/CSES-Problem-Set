def solve():
    MOD = 10**9 + 7
    n = int(input())
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(1,7):
            if i - j >= 0:
                dp[i] = (dp[i]%MOD + dp[i-j]%MOD)%MOD
    print(dp[n]) 

if __name__ == '__main__':
    solve()