import sys 
input = sys.stdin.readline
INF = float('inf')
def solve():
    n = int(input())
    if n == 0:
        print(0)
        return 
    if n == 1:
        print(1)
        return 
    dp = [INF]*(n+10)
    for i in range(1,10):
        dp[i] = 1 
    for i in range(10,n+1):
        j = i 
        while j:
            dp[i] = min(dp[i - j%10] + 1,dp[i])
            j //= 10  
     
    print(dp[n])
    

if __name__ == '__main__':
    solve()