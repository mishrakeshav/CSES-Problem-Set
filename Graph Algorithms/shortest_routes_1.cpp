#include<bits/stdc++.h>
using namespace std;
#define ll long long  
#define endl '\n'
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e15;

int n,m;
ll graph[MAX_N][MAX_N];
vector<ll> dist;


void dijikstras(int src){
    dist.assign(n + 1, LINF);
    dist[src] = 0;
    ll d;
    priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<pair<ll,ll>>> pq;
    pq.push(make_pair(0,src));
    while(!pq.empty()){
        auto [ds,node] = pq.top();
        pq.pop();
        if(ds > dist[node]) continue;
        for (auto [v, w] : graph[node]) {
            if (dist[v] > dist[node] + w) {
                dist[v] = dist[node] + w;
                pq.push({dist[v], v});
            }
        }
    }
}
void solve(){
 int u,v,w;
    cin >> n >> m;
    for(int i = 1; i <=m; i++){
        cin >> u >> v >> w;
        graph[u].push_back({v,w});
    }
    dijikstras(1);
    for(int i=1; i <= (int)n; i++){
        cout << dist[i] << " ";
    }
    cout << endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
   solve();
    return 0;
}