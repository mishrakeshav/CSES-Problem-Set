#include<bits/stdc++.h>
using namespace std;
int find_insertion_point(vector<int>& dp, int val){
    int low,high,mid;
    low = 0;
    high = dp.size()-1;
    int ans = high + 1;
    while(low<=high){
        mid = low + (high-low)/2;
        if(dp[mid] < val){
            ans = mid;
            low = mid + 1;
        }else{
            high = mid -1;
        }
    }
    return ans + 1;
}

int solve(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n+1,INT_MAX);
    dp[0]=INT_MIN;
    int max_size = 0;
    for(int i =0; i < n; i++){
        int size = find_insertion_point(dp,nums[i]);
        max_size = max(max_size,size);
        if(dp[size] > nums[i]){
            dp[size] = nums[i];
        }
    }
    return max_size;
}
int main(){
    int n;
    cin >> n;
    vector<int> arr(n,0);
    for(int i =0; i < n; i++){
        cin >> arr[i];
    }
    cout << solve(arr) << endl;
}

