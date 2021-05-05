from bisect import bisect_left,bisect_right,insort,bisect
x,n = map(int,input().split())
pos = list(map(int,input().split()))
arr = []
k = 0 
for i in pos:
    insort(arr,i)
    k = 0 
    for i in range(1,len(arr)):
        k = max(k,arr[i]-arr[i-1])
    k = max(arr[0],k)
    k = max(x-arr[-1],k)
    print(k)
    
