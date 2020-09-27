

def solve():
    n = int(input())
    customers = []
    for _ in range(n):
        a,b = map(int,input().split())
        customers.append([a,b])
    customers.sort()
    customers.sort(key = lambda x : x[1])
    ans = 1
    for i in range(1,n):
        if(customers[i-1][1] > customers[i][0]):
            ans += 1 
    


if __name__ == '__main__':
    solve()