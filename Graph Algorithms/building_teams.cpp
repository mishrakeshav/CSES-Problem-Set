#include<bits/stdc++.h>
#include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;
using namespace std;

class Vertex{
    public:
    int data;
    int visited;
    int group;
    vector<int> connections;
};

int dfs(unordered_map<int, Vertex>& graph, int n){
    int count = 0;
    stack<Vertex> s;
    for(int i = 1; i <= n; i++){
        if(graph[i].visited) continue;
        count++;
        s.push(graph[i]);
        graph[i].group = count;
        while(!s.empty()){
            Vertex v = s.top();
            s.pop();
            for(auto i: v.connections){
                if(graph[i].visited) continue;
                graph[i].visited = 1;
                graph[i].group = count; 
                s.push(graph[i]);
            }
        }
        
    }
    return count;
}
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int n, m,a,b;
    cin >> n >> m;
    unordered_map<int , Vertex> graph;
    for(int i = 0; i < n; i++){
        graph[i+1] = Vertex();
        graph[i+1].data = i+1;
        graph[i+1].visited = 0;
        graph[i+1].group = 0;
    }
    for(int i = 0 ; i < m; i++){
        cin >> a >> b;
        graph[a].connections.push_back(b);
        graph[b].connections.push_back(a);
    }
    int count = dfs(graph,n);
    if(count != 2){
        cout << "IMPOSSIBLE" << endl;
    }else{
        for(int i = 1; i <= n; i++){
            cout << graph[i].group << " ";
        }
        cout << endl;
    }
}