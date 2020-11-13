
import sys
input=sys.stdin.readline
def solve():
    MOD = 10**9 + 7
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))
    dp = [0]*(x+1)
    dp[0] = 1
    for i in coins:
        for j in range(i,x+1):
            dp[j] += dp[j-i]
            dp[j] %= MOD 
    print(dp[x]) 

if __name__ == '__main__':
    solve()