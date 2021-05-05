#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n,m;
    cin >> n >> m;
    vector<int> a(n),b(n);
    for(int &x : a){
        cin >> x;
        x--;
    }
    int ans = 1;
    for(int i = 0; i < n; i++){
        b[a[i]] = i;
    }
    for(int i = 1; i < n; i++){
        ans += b[i-1] > b[i];
    }
    while(m--){
        int p,q;
        cin >> p >> q;

    }
}