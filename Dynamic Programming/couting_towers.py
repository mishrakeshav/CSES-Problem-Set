def solve(n):
    if n == 0: return 1
    if n == 1: return 2
    ans = 0 
    upper = n//2 
    if n%2:
        upper += 1 
    for i in range(1,upper):
        ans += solve(i)*solve(n-i)
    return 1 + ans 

if __name__ == '__main__':
    for t in range(int(input())):
        print(solve(int(input())))