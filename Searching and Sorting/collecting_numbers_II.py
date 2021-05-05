"""
If the number x occurs before x+1 then you can always take both of them in a single
round and hence it won’t contribute anything to the answer but if x comes after x+1 
then we cannot take them in the single round hence we add 1 to the final answer.
"""
n,m = map(int,input().split())
arr = list(map(int,input().split()))
brr = [0 for i in range(n+1)]
ans = 1 

for i in range(n):
    brr[arr[i]-1] = i 

for i in range(1,n):
    ans += int(brr[i] < brr[i-1])

for i in range(m):
    a,b = map(int,input().split())
    a -= 1 
    b -= 1 
    idx1 = brr[a]
    idx2 = brr[b]
    plus = 0 
    minus = 0 
    
    if a != 0 and brr[a] < brr[a-1]:
        minus += 1 
    if a!=(n-1)  and brr[a+1] < brr[a]:
        minus += 1  
    if b!= 0 and brr[b] < brr[b-1] and a!=b-1:
        minus += 1  
    if b!= (n-1) and brr[b+1] < brr[b] and a!=b+1:
        minus += 1  
    
    brr[a] = idx2
    brr[b] = idx1
    
    if a != 0 and brr[a] < brr[a-1]:
        plus += 1 
    if a!=(n-1)  and brr[a+1] < brr[a]:
        plus += 1  
    if b!= 0 and brr[b] < brr[b-1] and a!=b-1:
        plus += 1  
    if b!= (n-1) and brr[b+1] < brr[b] and a!=b+1:
        plus += 1  
    
    ans = ans + plus - minus
    print(ans)


