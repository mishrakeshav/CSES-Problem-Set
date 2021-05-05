#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,x;
    cin >> n >> x;
    vector<int> a(n);
    for(int &x:a){
        cin >> x;
    }
    sort(a.begin(),a.end());
    int found = 0;
    for(int i = 0; i < n; i++){
        int y = x - a[i];
        int l ,m;
        l = 0; m = n-1;
        while (l < m){
            if(l == i){
                l++;
                continue;
            }
            if(m == i){
                m--;
                continue;
            }
            if(a[l] + a[m] == y){
                cout << i+1 << " " << l+1 << " " << m+1 << endl;
                found = 1;
                break;
            }else if(a[l] + a[m] < y){
                l++;
            }else{
                m--;
            }
        }
        if(found) break;
    }
    if(!found){
        cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}