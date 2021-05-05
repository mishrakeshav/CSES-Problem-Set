#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for(int &x : a){
        cin >> x; 
        x--;
    }
    for(int i = 0; i < n; i++){
        b[a[i]] = i;
    }
    int ans = 1;
    for(int i = 1; i < n; i++){
        ans += b[i] < b[i-1];
    }
    cout << ans << endl;
    return 0;
}