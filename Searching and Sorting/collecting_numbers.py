"""
If the number x occurs before x+1 then you can always take both of them in a single
round and hence it won’t contribute anything to the answer but if x comes after x+1 
then we cannot take them in the single round hence we add 1 to the final answer.
"""
n = int(input())
arr = list(map(int,input().split()))
brr = [0 for i in range(n+1)]
ans = 1 

for i in range(n):
    brr[arr[i]-1] = i 

for i in range(1,n):
    ans += int(brr[i] < brr[i-1])
print(ans)

