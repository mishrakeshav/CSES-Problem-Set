#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int mx = n*1000;
    vector<int> x(n);
    for(int i = 0; i < n; i++){
        cin >> x[i];
    }
    vector< vector<bool> > dp(n+1, vector<bool>(mx+1,false));
    dp[0][0] = true;
    for(int i = 1; i <=n; i++){
        for(int j = 0; j <= mx; j++){
            dp[i][j] = dp[i-1][j];
            if(j - x[i-1] >= 0){
                dp[i][j] = dp[i][j] || dp[i-1][j-x[i-1]];
            }
        }
    }
    vector<int> possible;
    for(int i = 1; i <= mx; i++){
        if(dp[n][i]){
            possible.push_back(i);
        }
    }
    cout << possible.size() << endl;
    for(int i = 0; i < possible.size(); i++){
        cout << possible[i] << " ";
    }
    cout << endl;
}