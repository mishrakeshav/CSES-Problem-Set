#include<bits/stdc++.h>
using namespace std;
int solve(int n){
    if(n == 0) return 1;
    if(n == 1) return 2;
    int ans = 0;
    for(int i = 1; i <= n; i++){
        ans += solve(n-i)*solve(i);
    }
    return ans;
}

int main(){
    
    int t,n;
    cin >> t;
    while(t--){
        cin >> n;
        cout << solve(n) << endl;
    }
    return 0;
}