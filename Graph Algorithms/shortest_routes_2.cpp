#include<bits/stdc++.h>
using namespace std;
#define ll long long  
#define endl '\n'
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e15;
const int nax = 5e2+5;

int n,m,q;
ll graph[nax][nax];

void shortestpath(){
    for(int i = 1; i<=n; i++){
        graph[i][i] = 0;
    }
    for(int k = 1; k <=n; k++){
        for(int i = 1; i <=n; i++){
            for(int j = 1; j<=n; j++){
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
}
void solve(){
    ll u,v,w;
    cin >> n >> m >> q;
    for(int i = 1; i <= n; i++ ){
        for(int j = 1; j <= n; j++){
            graph[i][j] = LINF;            
        }
    }
    for(int i = 1; i <=m; i++){
        cin >> u >> v >> w;
        graph[u][v] = min(graph[u][v],w);
        graph[v][u] = min(graph[u][v],w);
    }
    shortestpath();
    for(int i = 0; i < q; i++){
        cin >> u >> v;
        if(graph[u][v]!=LINF){
            cout << graph[u][v] << endl; 
        }
        else{
            cout << -1 << endl;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    solve();
    return 0;
}