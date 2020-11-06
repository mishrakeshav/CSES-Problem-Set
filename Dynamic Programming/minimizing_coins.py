def solve():
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))
    coins.sort()
    dp = [float("inf")]*(x+1)
    dp[0] = 0 
    for i in range(x+1):
        for j in coins:
            if i - j >= 0:
                dp[i] = min(dp[i],dp[i-j] + 1)
            else:
                break
    if dp[x] == float("inf"):
        print(-1)
        return 
    print(dp[x])


if __name__ == '__main__':
    solve()