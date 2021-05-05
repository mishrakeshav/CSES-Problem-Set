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
char adj[1010][1010],path[1010][1010];
int dist[1010][1010], d[1010][1010], visited[1010][1010];

char getPath(int a,int b){
    if(a == -1 && b == 0){
        return 'D';
    }else if(a == 1 && b == 0){
        return 'U';
    }else if(a == 0 && b == -1){
        return 'R';
    }else if(a == 0 && b == 1){
        return 'L';
    }
}


void dfs(int i, int j, int monster){
    for(int a = 0; a < n ; a++){
        for(int b = 0; b < m; b++){
            visited[a][b] = 0;
        }
    }
    int dx[] = {1,-1,0,0};
    int dy[] = {0,0,1,-1};
    vector<tuple<int,int,int>> arr;
    arr.emplace_back(i,j,0);
    while(arr.size()!=0){
        tuple<int,int,int> uvh = arr[arr.size()-1];
        int u = get<0>(uvh);
        int v = get<1>(uvh);
        int h = get<2>(uvh);
        arr.pop_back();
        if(visited[u][v]==1) continue;
        visited[u][v] = 1;
        if(monster==1){
            dist[u][v] = min(dist[u][v],h);
        }else{
            d[u][v] = min(d[u][v],h);
        }
        for(int k = 0; k < 4; k++){
            int y = u + dy[k];
            int x = v + dx[k];
            if( x >= 0 && x < m &&  y < n && y >=0 && adj[y][x]!='#'){
                arr.emplace_back(y,x,h+1);
                if(monster==0){
                    path[y][x] = getPath(u-y,v-x);
                    cout << y << " " << x << " "<< path[y][x] << endl;
                }
            }
        }
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i <n; i++){
        for(int j = 0; j < m; j++){
            cin >> adj[i][j];
            dist[i][j] = INF;
            d[i][j] = INF;
            path[i][j] = '#';
        }
    }
    int a,b;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(adj[i][j] == 'M'){
                dfs(i,j,1);
            }else if(adj[i][j]=='A'){
                a = i;
                b = j;
                path[i][j] = 'A';
            }
        }
    }
    dfs(a,b,0);
    path[a][b] = 'A';
    int ans = 0;
    int ei,ej;
    for(int i = 0; i <n && ans ==0; i++){
        if(dist[i][0] > d[i][0]){
            a = i;
            b = 0;
            ans = 1;
        }
        if(dist[i][m-1] > d[i][m-1]){
            ans = 1;
            a = i;
            b = m-1;
        }
    }
    for(int i = 0; i <m && ans ==0; i++){
        if(dist[0][i] > d[0][i]){
            ans = 1;
            a = 0;
            b = i;
        }
        if(dist[n-1][i] > d[n-1][i]){
            ans = 1;
            a = n-1;
            b = i;
        }
    }
    if(ans==1){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(path[i][j]=='\0'){
                cout << "#";
            }else{
                cout << path[i][j] << " ";
            }
        }
            cout << endl;
    }
    // vector<char> p;
    // while(path[a][b] != 'A'){
    //     p.push_back(path[a][b]);
    //     cout << path[a][b] << endl;
    //     if(path[a][b] == 'U'){
    //         a += 1;
    //     }else if(path[a][b]=='D'){
    //         a -= 1;
    //     }else if(path[a][b]=='L'){
    //         b +=1;
    //     }else{
    //         b -= 1;
    //     }
    // }
    // for(int i =0; i < p.size(); i++){
    //     cout << p[i] << endl;
    // }
    return 0;
}
